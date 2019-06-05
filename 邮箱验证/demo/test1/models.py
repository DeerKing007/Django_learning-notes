# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TUser(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='用户的注册时间')
    has_confirmed = models.BooleanField(default=False, verbose_name='用户是否激活')

    class Meta:
        db_table = 't_user'


class ConfirmedString(models.Model):
    code = models.CharField(max_length=256, verbose_name='用户注册时生成的验证码')
    user = models.OneToOneField("TUser", on_delete=models.CASCADE, verbose_name='关联的用户')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='验证码生成的时间')

    class Meta:
        db_table = 't_confirmedString'

