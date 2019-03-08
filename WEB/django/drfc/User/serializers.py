from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """

    class Meta:
        model = User
        fields = ("id", "username", "gender", "mobile", "birthday", "email")


class UserRegSerializer(serializers.ModelSerializer):
    # code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
    #                              error_messages={
    #                                  "blank": "请输入验证码",
    #                                  "required": "请输入验证码",
    #                                  "max_length": "验证码格式错误",
    #                                  "min_length": "验证码格式错误"
    #                              },
    #                              help_text="验证码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    class Meta:
        model = User
        fields = ("username", "mobile", "password")
        # fields = ("username", "code", "mobile", "password")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
