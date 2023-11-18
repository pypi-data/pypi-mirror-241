import argparse
import copy
import datetime
import logging
import os
import re

import torch
import torch.distributed as dist
import torch.optim as optim
import yaml
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from ..config.gxl_config import GxlNode
from ..utils import utils_file
from ..gxl_dataset_wenet.gxl_dataset import GxlAsrDataset
from ..gxl_model_wenet.init_model import init_model, ASRModel
from ..gxl_model_wenet.utils.executor import Executor
from ..gxl_model_wenet.utils.checkpoint import load_checkpoint, save_checkpoint, load_trained_modules
from ..gxl_lr_scheduler_wenet.scheduler import WarmupLR, NoamHoldAnnealing
from ..utils import utils_data


def read_non_lang_symbols(non_lang_sym_path):
    """read non-linguistic symbol from file.
    The file format is like below:
    {NOISE}\n
    {BRK}\n
    ...
    Args:
        non_lang_sym_path: non-linguistic symbol file path, None means no any
        syms.
    """
    if non_lang_sym_path is None:
        return None
    else:
        syms = utils_file.load_list_file_clean(non_lang_sym_path)
        non_lang_syms_pattern = re.compile(r"(\[[^\[\]]+\]|<[^<>]+>|{[^{}]+})")
        for sym in syms:
            if non_lang_syms_pattern.fullmatch(sym) is None:
                class BadSymbolFormat(Exception):
                    pass

                raise BadSymbolFormat(
                    "Non-linguistic symbols should be "
                    "formatted in {xxx}/<xxx>/[xxx], consider"
                    " modify '%s' to meet the requirment. "
                    "More details can be found in discussions here : "
                    "https://github.com/wenet-e2e/wenet/pull/819" % (sym))
        return syms


def read_symbol_table(symbol_table_file):
    symbol_table = {}
    with open(symbol_table_file, 'r', encoding='utf8') as fin:
        for line in fin:
            arr = line.strip().split()
            assert len(arr) == 2
            symbol_table[arr[0]] = int(arr[1])
    return symbol_table


class GxlTrainer(object):
    def __init__(self, train_config_yaml_path: str):
        self.args = GxlNode.get_config_from_yaml(train_config_yaml_path)
        print(f'self.args:\n {self.args}')
        torch.manual_seed(777)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(message)s')
        self.configs = GxlNode.get_config_from_yaml(self.args.content_config)

    def prepare_data(self, train_wav_scp_path: str, train_text_scp_path: str,
                     cv_wav_scp_path: str, cv_text_scp_path: str, ):
        """
        数据处理：
        1. 移除text_scp中的空白间隔，如果没有空白间隔，则不作为
        2. 根据配置文件中的设置选择是否计算cmvn
        3. 提取训练集和验证集文本中的token并得到token_symbol_table文件
        4. 最后得到dataset需要的data.list数据。
        :param train_wav_scp_path:
        :param train_text_scp_path:
        :param cv_wav_scp_path:
        :param cv_text_scp_path:
        :return:
        """
        utils_data.do_remove_blank_for_text_scp(train_text_scp_path)
        utils_data.do_remove_blank_for_text_scp(cv_text_scp_path)
        if self.args.cmvn is not None:
            utils_data.do_compute_cmvn_stats(self.args.num_workers, self.args.content_config,
                                             train_wav_scp_path, self.args.cmvn)

        utils_data.do_text2token(train_text_scp_path, self.args.symbol_table)

        utils_data.do_make_raw_list(train_wav_scp_path, train_text_scp_path, self.args.train_data)
        utils_data.do_make_raw_list(cv_wav_scp_path, cv_text_scp_path, self.args.cv_data)

    def train_run(self):
        args = self.args
        configs = self.configs

        world_size = int(os.environ.get('WORLD_SIZE', 1))  # gpu数量
        local_rank = int(os.environ.get('LOCAL_RANK', 0))  # 本机范围内序号
        rank = int(os.environ.get('RANK', 0))  # 全局范围内序号
        distributed = world_size > 1
        if distributed:
            logging.info('training on multiple gpus, this gpu {}'.format(local_rank))
            torch.cuda.set_device(local_rank)
            dist.init_process_group(args.dist_backend,
                                    init_method=args.init_method,
                                    world_size=world_size,
                                    rank=rank)
        symbol_table = read_symbol_table(args.symbol_table)
        train_conf = configs['dataset_conf']
        cv_conf = train_conf.copy()
        cv_conf['speed_perturb'] = False
        cv_conf['spec_aug'] = False
        cv_conf['spec_sub'] = False
        cv_conf['spec_trim'] = False
        cv_conf['shuffle'] = False
        non_lang_syms = read_non_lang_symbols(args.non_lang_syms)
        train_dataset = GxlAsrDataset(args.data_type, args.train_data, symbol_table,
                                      train_conf, args.bpe_model, non_lang_syms, True)
        cv_dataset = GxlAsrDataset(args.data_type,
                                   args.cv_data,
                                   symbol_table,
                                   cv_conf,
                                   args.bpe_model,
                                   non_lang_syms,
                                   partition=False)

        train_data_loader = DataLoader(train_dataset,
                                       batch_size=None,
                                       pin_memory=args.pin_memory,
                                       num_workers=args.num_workers,
                                       prefetch_factor=args.prefetch)
        cv_data_loader = DataLoader(cv_dataset,
                                    batch_size=None,
                                    pin_memory=args.pin_memory,
                                    num_workers=args.num_workers,
                                    prefetch_factor=args.prefetch)

        if 'fbank_conf' in configs['dataset_conf']:
            input_dim = configs['dataset_conf']['fbank_conf']['num_mel_bins']
        else:
            input_dim = configs['dataset_conf']['mfcc_conf']['num_mel_bins']
        vocab_size = len(symbol_table)
        # Save configs to model_dir/train.yaml for inference and export
        configs['input_dim'] = input_dim
        configs['output_dim'] = vocab_size
        configs['cmvn_file'] = args.cmvn
        configs['is_json_cmvn'] = True
        configs['lfmmi_dir'] = args.lfmmi_dir
        if rank == 0:
            saved_config_path = os.path.join(args.model_dir, 'train.yaml')
            utils_file.makedir_for_file(saved_config_path)
            with open(saved_config_path, 'w') as fout:
                data = yaml.dump(configs.dict())
                fout.write(data)
        # Init asr model from configs
        model = init_model(configs)
        print(model) if local_rank == 0 else None
        num_params = sum(p.numel() for p in model.parameters())
        if isinstance(model, ASRModel) and local_rank == 0:
            num_params_encoder = sum(p.numel() for p in model.encoder.parameters())
            num_params_decoder = sum(p.numel() for p in model.decoder.parameters())
            print(f'the number of model params:total:{num_params}, encoder:{num_params_encoder},decoder:{num_params_decoder}') # noqa
        # !!!IMPORTANT!!!
        # Try to export the model by script, if fails, we should refine
        # the code to satisfy the script export requirements
        if rank == 0:
            script_model = torch.jit.script(model)
            script_model.save(os.path.join(args.model_dir, 'init.zip'))

        executor = Executor()
        # If specify checkpoint, load some info from checkpoint
        if args.checkpoint is not None:
            infos = load_checkpoint(model, args.checkpoint)
        elif args.enc_init is not None:
            logging.info('load pretrained encoders: {}'.format(args.enc_init))
            infos = load_trained_modules(model, args)
        else:
            infos = {}
        start_epoch = infos.get('epoch', -1) + 1
        cv_loss = infos.get('cv_loss', 0.0)
        step = infos.get('step', -1)

        num_epochs = configs.get('max_epoch', 100)
        model_dir = args.model_dir
        writer = None
        if rank == 0:
            os.makedirs(model_dir, exist_ok=True)
            exp_id = os.path.basename(model_dir)
            writer = SummaryWriter(os.path.join(args.tensorboard_dir, exp_id))

        if distributed:  # native pytorch ddp
            assert (torch.cuda.is_available())
            # cuda model is required for nn.parallel.DistributedDataParallel
            model.cuda()
            model = torch.nn.parallel.DistributedDataParallel(
                model, find_unused_parameters=True)
            device = torch.device("cuda")
            if args.fp16_grad_sync:
                from torch.distributed.algorithms.ddp_comm_hooks import (
                    default as comm_hooks,
                )
                model.register_comm_hook(
                    state=None, hook=comm_hooks.fp16_compress_hook
                )
        else:
            use_cuda = torch.cuda.is_available()
            device = torch.device('cuda' if use_cuda else 'cpu')
            model = model.to(device)

        if configs['optim'] == 'adam':
            optimizer = optim.Adam(model.parameters(), **configs['optim_conf'])
        elif configs['optim'] == 'adamw':
            optimizer = optim.AdamW(model.parameters(), **configs['optim_conf'])
        else:
            raise ValueError("unknown optimizer: " + configs['optim'])
        scheduler_type = None
        if configs['scheduler'] == 'warmuplr':
            scheduler_type = WarmupLR
            scheduler = WarmupLR(optimizer, **configs['scheduler_conf'])
        elif configs['scheduler'] == 'NoamHoldAnnealing':
            scheduler_type = NoamHoldAnnealing
            scheduler = NoamHoldAnnealing(optimizer, **configs['scheduler_conf'])
        else:
            raise ValueError("unknown scheduler: " + configs['scheduler'])
        final_epoch = None
        configs['rank'] = rank
        configs['is_distributed'] = distributed  # pytorch native ddp
        configs['use_amp'] = args.use_amp
        if start_epoch == 0 and rank == 0:
            save_model_path = os.path.join(model_dir, 'init.pt')
            save_checkpoint(model, save_model_path)
        # Start training loop
        executor.step = step
        scheduler.set_step(step)
        # used for pytorch amp mixed precision training
        scaler = None
        if args.use_amp:
            scaler = torch.cuda.amp.GradScaler()

        for epoch in range(start_epoch, num_epochs):
            train_dataset.set_epoch(epoch)
            configs['epoch'] = epoch
            lr = optimizer.param_groups[0]['lr']
            logging.info('Epoch {} TRAIN info lr {}'.format(epoch, lr))
            device = model.local_rank if args.deepspeed else device
            executor.train(model, optimizer, scheduler, train_data_loader, device,
                           writer, configs, scaler)
            total_loss, num_seen_utts = executor.cv(model, cv_data_loader, device,
                                                    configs)
            cv_loss = total_loss / num_seen_utts

            logging.info('Epoch {} CV info cv_loss {}'.format(epoch, cv_loss))
            infos = {
                'epoch': epoch, 'lr': lr, 'cv_loss': cv_loss, 'step': executor.step,
                'save_time': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            }
            if rank == 0:
                writer.add_scalar('epoch/cv_loss', cv_loss, epoch)
                writer.add_scalar('epoch/lr', lr, epoch)
                with open("{}/{}.yaml".format(model_dir, epoch), 'w') as fout:
                    data = yaml.dump(infos)
                    fout.write(data)
            if args.deepspeed and rank == 0:
                save_model_path = os.path.join(model_dir, '{}.pt'.format(epoch))
                save_checkpoint(model, save_model_path, infos)
            final_epoch = epoch

        if final_epoch is not None and rank == 0:
            final_model_path = os.path.join(model_dir, 'final.pt')
            os.remove(final_model_path) if os.path.exists(final_model_path) else None
            os.symlink('{}.pt'.format(final_epoch), final_model_path)
            writer.close()


