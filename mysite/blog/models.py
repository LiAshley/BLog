from django.db import models
# 导入User
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
# 富文本编辑引入包
from ckeditor_uploader.fields import RichTextUploadingField
# 类型表，因为外键的关系，类型表要在博客表之前创建
class BaseType(models.Model):
    type_name = models.CharField(max_length=50,verbose_name='类型名称')

    class Meta:
        verbose_name = "博客大类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name
class BlogType(models.Model):
    type_name = models.CharField(max_length=50,verbose_name='类型名称')
    base_type = models.ForeignKey(BaseType,null=True,on_delete = models.DO_NOTHING)

    class Meta:
        verbose_name = "博客细类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name




# 博客表
class Blog(models.Model):
    title = models.CharField(max_length=30,verbose_name='标题')
    blog_type = models.ForeignKey(BlogType,on_delete = models.DO_NOTHING)
    # content = models.CharField() CharField必须定义max_length
    content = RichTextUploadingField() #正文不限制字数
    author = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    # created_time = models.DateTimeField(auto_now_add = True)
    # last_updated_time = models.DateTimeField(auto_now = True)
    created_time = models.DateTimeField(default = timezone.now,verbose_name='创建日期')
    last_updated_time = models.DateTimeField(default = timezone.now)
    # 是否显示
    # isShow = models.BooleanField(default=True,verbose_name="是否显示")
    class Meta:
        verbose_name="博客表"
        verbose_name_plural=verbose_name