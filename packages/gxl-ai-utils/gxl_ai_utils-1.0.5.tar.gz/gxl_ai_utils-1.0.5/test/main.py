from gxl_ai_utils.gxl_trainer_wenet import gxl_trainer
from gxl_ai_utils.utils import utils_data, utils_file

if __name__ == '__main__':
    """"""
    runner = gxl_trainer.GxlTrainer("./train_config.yaml")
    runner.prepare_data("./data/train/wav.scp", "./data/train/text.scp", "./data/dev/wav.scp", "./data/dev/text.scp")
    # data_path = 'E:\gengxuelong_study\server_local_adapter\\ai\data\small_aishell'
    # utils_data.get_scp_for_wav_dir(data_path+'/train', './data/train/wav.scp')
    # utils_data.get_scp_for_wav_dir(data_path+'/dev', './data/dev/wav.scp')
    # utils_data.get_scp_for_wav_dir(data_path+'/test', './data/test/wav.scp')
    runner.train_run()
