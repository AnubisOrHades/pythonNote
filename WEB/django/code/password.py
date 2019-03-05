from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from WEB.django.drfc.User.models import User

username = input("请输入账号")
password = input("请输入密码")

# 注册
user = User()
user.password = make_password(password)  # 明文密码经过加密处理
user.save()

# 登录
user = authenticate(username=username, password=password)
