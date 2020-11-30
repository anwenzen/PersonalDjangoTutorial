# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    details = models.CharField(max_length=100, verbose_name='详细信息')
    content = models.CharField(max_length=3000, verbose_name='内容')
    date = models.DateField(verbose_name='日期')
    author = models.CharField(max_length=20, verbose_name='作者')

    def __str__(self):
        return self.title

