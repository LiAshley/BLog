from django.shortcuts import render,get_object_or_404
from .models import Blog,BlogType,BaseType
from django.core.paginator import Paginator,PageNotAnInteger,InvalidPage,EmptyPage
# Create your views here.
'''设置get方法'''


def gobal(request):
    ''' 获取所有的大分类'''
    base_types = BaseType.objects.all()

    # print(base_categorys)
    
    ''' 获取所有的细分类'''
    all_categorys = BlogType.objects.all()
    # print(all_categorys)
   
    ''
    ''' 获取大分类下的细分类'''
     
    ''' 获取所有的日期'''
    all_dates = Blog.objects.dates("created_time", 'month', order='DESC')
    ''' 获取所有的文章'''
    all_blogs = Blog.objects.all().order_by('-created_time')
    ''' 获取最近五篇文章'''
    recent_blogs = all_blogs[:5]
    '''dates(field, kind, order='ASC')三个参数为：字段，类型，和排序方法，ASC（正序）和DESC（倒序）'''
    all_dates = Blog.objects.dates("created_time", 'month', order='DESC')
    return locals()
'''分页封装方法'''
def pag(request1, objForPag, num):
    '''返回了两个值，有三个参数，调用传入三个参数，并自定义两个两个而接受返回值'''
    '''参数1、网页获取对象，2、需要分页（all_list）的对象，3、分页每页的数据'''
    '''返回值1、获取当页对象，2、循环的页数'''
    '''分页'''
    # 1、实例化分页器 第一个参数是要分页的对象，第二个参数每页的博客对象数量
    paginator = Paginator(objForPag, num)
    # 2、获取当前页码
    try:
        page_num = request1.GET.get("page", 1)
        # 3、通过当前页码获取当页的对象（不是具体数据，所以不能直接得出数量等）
        pageObj = paginator.page(page_num)
        '''实现页码不全部显示，只显示前后两页.默认是全部显示blog_list.paginator.page_range方法全部获得'''
        currentPage = pageObj.number  # 获取当前页码
        # page_range = [max(currentPage-2,1),currentPage-1,currentPage,currentPage+1,currentPage+2]#循环遍历的部分
        page_range = list(range(max(currentPage - 2, 1), currentPage)) + list(
            range(currentPage, min(currentPage + 2, paginator.num_pages) + 1))

        # 加上省略号
        if page_range[0] - 1 >= 2:
            page_range.insert(0, '...')
        if paginator.num_pages - page_range[-1] >= 2:
            page_range.append('...')

        # 加上首尾页码
        if page_range[0] != 1:
            page_range.insert(0, 1)  # 0位置，插入1数字
        if page_range[-1] != paginator.num_pages:
            page_range.append(paginator.num_pages)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        pageObj = paginator.page(1)
    return (pageObj, page_range)

'''分页结束'''


'''所有分类'''
def all_categorys(request):
    return render(request,'all_categorys.html',locals())
'''文章详情页面'''
def blog_post(request,blog_id):
    # obj = Blog.objects.get(pk = blog_id)
    obj = get_object_or_404(Blog,id = blog_id)
    '''获取上一篇下一篇'''
    blog_prev = Blog.objects.filter(created_time__gt=obj.created_time).first()
    blog_next = Blog.objects.filter(created_time__lt=obj.created_time).last()
    '''显示归档'''
    
    '''显示所属分类'''


    return render(request,'blog_post.html',locals())

'''所有博客列表'''
def blog_list(request):
    # all_categorys = get_all_categorys()
    all_blogs = Blog.objects.all().order_by("-created_time")
    '''分页显示'''
    pageObj, page_range = pag(request,all_blogs,10)
    '''显示归档'''
    

    return render(request,'blog_list.html',locals())

'''归档下博客'''
def archieve_blogs(request,year,month):
    '''显示归档'''
    
    date_blogs = Blog.objects.filter(created_time__year=year, created_time__month=month)
    date = "%s年%s月" % (year, month)
    '''分页显示'''
    pageObj, page_range = pag(request, date_blogs, 10)

    return render(request,'archieve_blogs.html',locals())



'''得到大类下小类'''
def base_categorys(request,pk):

    # 根据大类id，得到该大类下的所有小类
    base_type_name = BaseType.objects.get(pk = pk)#大类

    base_categorys = BlogType.objects.filter(base_type = base_type_name)
    # print(base_categorys)

    return render(request,'base_categorys.html',locals())


def category_blogs(request,id):

    # 1.得到类型---filter得到一个列表(不是对象，不能直接点属性),所以就算只有一个值,也要切片取值
    typename = BlogType.objects.filter(pk = id).first()


    # 2.通过外键得到对象博客
    category_blogs = Blog.objects.filter(blog_type = typename)#过滤器

    '''分页'''
    pageObj, page_range = pag(request, category_blogs, 10)

    # 通过子表（小类型）查询父表（大类型),已知下类型的id
    cateObj = BlogType.objects.get(pk=id) # 得到当前小分类的对象
    
    baseObj = BaseType.objects.get(type_name = cateObj.base_type)#获取当前大类对象
  
    base_categorys = baseObj.blogtype_set.all()


    return render(request,'category_blogs.html',locals())



def bootstrap(request):

    
    return render(request,'bootstrap.html',locals())

# def archives(request):
#     '''显示归档'''
#     
#     return render(request,'archives.html',locals())


def waiting2(request):
    
    '''显示归档'''
    
    return render(request,'waiting2.html',locals())

def waiting3(request):
    
    '''显示归档'''
    
    return render(request,'waiting3.html',locals())

def waiting4(request):
    
    '''显示归档'''
    
    return render(request,'waiting4.html',locals())
