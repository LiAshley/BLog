from django.shortcuts import render
from blog.models import BlogType,Blog
def home(request):
    '''显示所有的分类'''
    all_categorys = BlogType.objects.all()
    '''最新文章'''
    recent_blogs = Blog.objects.all().order_by()[:5]
    return render(request,'index.html',locals())



