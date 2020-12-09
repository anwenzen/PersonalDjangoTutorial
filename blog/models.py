from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    details = models.CharField(max_length=100, verbose_name='详细信息')
    content = models.CharField(max_length=3000, verbose_name='内容')
    date = models.DateField(verbose_name='日期')
    author = models.CharField(max_length=20, verbose_name='作者')

    def __str__(self):
        return self.title

