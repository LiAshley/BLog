from django.contrib import admin
from .models import BlogType,Blog
# Register your models here.


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['pk','type_name']
    list_editable=['type_name']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 显示项,默认只有一个对象
    list_display = ['pk','title','blog_type','created_time']
    # 可编辑项,注:必须list_display后,才能编辑
    list_editable=['title','blog_type','created_time']
    # admin列表分页显示
    list_per_page=10#admin页面分页显示
    # 后台数据排序
    # ordering = ["-created_time"]
    ordering = ["-pk"]


# admin.site.register(BlogType)
# admin.site.register(Blog)
