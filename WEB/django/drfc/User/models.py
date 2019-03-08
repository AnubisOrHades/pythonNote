from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    userAddress = models.CharField(max_length=100, null=True, blank=True, verbose_name="用户地址")
    remarks = models.CharField(max_length=50, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Book(models.Model):
    bookName = models.CharField(max_length=20, verbose_name="书名")
    synopsis = models.TextField(verbose_name="简介")
    auth = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "书籍信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bookName
