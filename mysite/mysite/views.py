from django.shortcuts import render
from blog.models import BlogType,Blog,BaseType

def gobal(request):
    ''' 获取所有的大分类'''
    base_types = BaseType.objects.all()
    # print(base_categorys)
    
    ''' 获取所有的细分类'''
    all_categorys = BlogType.objects.all() 
     
    ''' 获取所有的日期'''
    all_dates = Blog.objects.dates("created_time", 'month', order='DESC')
    ''' 获取所有的文章'''
    all_blogs = Blog.objects.all().order_by('-created_time')
    ''' 获取最近五篇文章'''
    recent_blogs = all_blogs[:5]
    '''dates(field, kind, order='ASC')三个参数为：字段，类型，和排序方法，ASC（正序）和DESC（倒序）'''
    all_dates = Blog.objects.dates("created_time", 'month', order='DESC')
    return locals()

def home(request):
    return render(request,'index.html',locals())




