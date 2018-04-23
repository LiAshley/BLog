from django.shortcuts import render
from blog.models import BlogType,Blog

class getObj():
    def get_all_categorys():
        all_categorys = BlogType.objects.all()
        return all_categorys

    def get_all_blogs():
        all_categorys = BlogType.objects.all()
        return all_categorys

    def get_all_tags():
        all_categorys = BlogType.objects.all()
        return all_categorys

    def get_all_dates():
        '''dates(field, kind, order='ASC')三个参数为：字段，类型，和排序方法，ASC（正序）和DESC（倒序）'''
        all_dates = Blog.objects.dates("created_time", 'month', order='DESC')
        return all_dates

def home(request):
    '''显示所有的分类'''
    all_categorys = getObj.get_all_categorys()
    # print(all_categorys)
    '''最新文章'''
    recent_blogs = Blog.objects.all().order_by("-created_time")[:5]
    # print(recent_blogs)
    '''日期归档'''
    all_dates = getObj.get_all_dates()

    # print(all_dates)

    return render(request,'index.html',locals())



