# from distutils.core import setup
from setuptools import setup, find_packages

# packages = ['gxl_ai_utils', 'gxl_ai_utils.utils',
#             'gxl_ai_utils.config', 'gxl_ai_utils.run',
#             'gxl_ai_utils.thread', 'gxl_ai_utils.gxl_dataset_wenet',
#             'gxl_ai_utils.gxl_lr_scheduler_wenet', 'gxl_ai_utils.gxl_model_wenet',
#             'gxl_ai_utils.gxl_trainer_wenet', ]
setup(name='gxl_ai_utils',
      version='1.0.5',
      author='Xuelong Geng',
      description='这个工具包模块是耿雪龙的, 耿雪龙是小睿宝的. 含有模型训练,lr_schuduler,数据处理,通用方法, 常用模型等功能',
      author_email='3349495429@qq.com',
      packages=find_packages(),
      package_dir={'requests': 'requests'}, )
