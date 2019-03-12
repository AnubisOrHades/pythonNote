# 独立使用django的model
import sys
import os

# 项目名称
PROJECT = "drfc"
# 获取当前路径
pwd = os.path.dirname(os.path.realpath(__file__))
# 获取上一级目录
parent_path = os.path.dirname(pwd)
# 拼接项目路径
path = "{}\\{}\\{}".format(parent_path, PROJECT, PROJECT)
print(pwd, "\n", path)
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{}.settings").format(PROJECT)

import django

django.setup()

# from user.models import User

