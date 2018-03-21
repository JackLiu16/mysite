#coding=utf-8
from django.db import models
from ckeditor.fields import RichTextField
import django.utils.timezone as timezone

# Create your models here.

class Article(models.Model):
    '''日志'''
    title = models.CharField(verbose_name='标题', max_length=150, blank=False, null=False)
    content = RichTextField('正文') # 使用ckeditor中的RichTextField
    timestamp = models.DateTimeField('保存日期',default=timezone.now,blank=False, null=False)

    def __unicode__(self):
        return self.title