from django.db import models


# Create your models here.


class Position(models.Model):
    position_id = models.AutoField(verbose_name='职位ID', primary_key=True)
    position_name = models.CharField(max_length=50, verbose_name='职位名称')
    # company_id = models.AutoField(verbose_name='公司ID')
    company_full_name = models.CharField(max_length=50, verbose_name='公司名称')
    industry_field = models.CharField(max_length=50, verbose_name='行业领域')
    company_label_list = models.CharField(max_length=100, verbose_name='福利待遇')
    first_type = models.CharField(max_length=15, verbose_name='职位类型一')
    second_type = models.CharField(max_length=15, verbose_name='职位类型二')
    third_type = models.CharField(max_length=15, verbose_name='职位类型三')
    city = models.CharField(max_length=20, verbose_name='城市')
    district = models.CharField(max_length=50, verbose_name='区域')
    salary = models.CharField(max_length=15, verbose_name='薪资')
    work_year = models.CharField(max_length=20, verbose_name='工作经验')
    job_nature = models.CharField(max_length=50, verbose_name='工作性质')
    education = models.CharField(max_length=20, verbose_name='学历要求')
    create_time = models.CharField(max_length=20, verbose_name='发布时间')
    skill_labels = models.CharField(max_length=100, verbose_name='技能标签')
    latitude = models.CharField(max_length=12, verbose_name='纬度')
    longitude = models.CharField(max_length=12, verbose_name='经度')
