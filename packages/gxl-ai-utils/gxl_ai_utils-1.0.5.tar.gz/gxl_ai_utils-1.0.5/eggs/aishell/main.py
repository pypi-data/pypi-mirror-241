from gxl_ai_utils import gxl_trainer_wenet

runner = gxl_trainer_wenet.GxlTrainer("./train_config.yaml")


def handle_data():
    runner.prepare_data("./data/train/wav.scp", "./data/train/text.scp",
                        "./data/dev/wav.scp", "./data/dev/text.scp")


if __name__ == '__main__':
    """"""
    # handle_data()
    runner.train_run()
