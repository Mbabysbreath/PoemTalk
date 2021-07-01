from django.shortcuts import render
from django.views.generic.base import View
from bbs.models import  CategoryModel,ArticleModel
from operations.models import UserLove,UserComment
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.utils.decorators import method_decorator
from django.shortcuts import reverse,render,redirect
from tools.decorators import login_decorator
from datetime import date
# Create your views here.
class BBSIndexView(View):
    def get(self,request):
        categories = CategoryModel.objects.all()
        today = date.today()
        for category in categories:
            category.today = ArticleModel.objects.filter(category=category,publish_time__gte=today).count()
            category.total = ArticleModel.objects.filter(category=category).count()
        context = {
            'categories':categories
        }
        return render(request,'bbs/bbs-index.html',context)
def artical_list(request,cat_id):
    # 1.获取分类id
    # cat_id = request.GET.get('cat_id')
    # 2.根据分类id查询分类数据
    category=CategoryModel.objects.filter(id=cat_id)[0]
    # 3.根据分类id查询文章数据
    today = date.today()
    article_list = ArticleModel.objects.filter(category=category).order_by('-publish_time')
    today = ArticleModel.objects.filter(category=category, publish_time__gte=today).count()
    total = ArticleModel.objects.filter(category=category).count()
    for article in article_list:
        # 最后回复时间
        comments = UserComment.objects.filter(comment_article=article).order_by('-add_time')
        cm = comments.first()
        if cm is not None:
            article.last_comment_time = cm.add_time
        else:
            article.last_comment_time = '暂无回复'
        # 回复数量
        article.comments = len(comments)
        article.save()
    #     按评论数量排序选前五
    hot_articles = ArticleModel.objects.filter(category=category).order_by('-comments')[:5]
    print("评论前5",hot_articles)
    for hot_article in hot_articles:
        print(hot_article.title,"==",hot_article.comments,"==",hot_article.read_count,"=",hot_article.publish_time)
    # 分页
    pagenum = request.GET.get('pagenum', '')
    print("pagenum=", pagenum)
    print("pagenumtype=", type(pagenum))
    # 实例化对象，每页5个，在这里可以知道有多少页了
    pa = Paginator(article_list, 5)
    try:
        print("=====pages1======")
        pages = pa.page(pagenum)  # 取前台传过来的页数，如果不是整数或有效对象时抛出异常
        print("pages1=", pages)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        pages = pa.page(1)
        print("pages2=", pages)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pages = pa.page(pa.num_pages)
        print("pages3=", pages)

    # 4.组织上下文
    context = {
        'article_list': article_list,
        'category': category,
        'today': today,
        'total': total,
        'hot_articles':hot_articles,
        'pages':pages
    }
    return render(request, 'bbs/list.html', context=context)
@method_decorator(login_decorator,name='dispatch',)
class PublishView(View):
    def get(self,request):
        categories = CategoryModel.objects.all()
        context = {
            'categories': categories
        }

        return render(request, 'bbs/publish.html', context)

    def post(self,request):
        user_id = request.user.id
        print("====id:")
        print(user_id)

        category_id = request.POST.get('category_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        print("=========文章：")
        print(category_id)
        print(title)
        print(content)
        if not all([category_id,title,content]):
            print("=========文章： qqq")
            return render(request,'bbs/publish.html')
        try:
            category = CategoryModel.objects.get(pk = category_id)
        except CategoryModel.DoesNotExist:
            render(request,'bbs/publish.html')


        artical = ArticleModel.objects.create(
            title = title,
            content = content,
            category = category,
            user_id = user_id
        )
        artical.save()
        return redirect(reverse('bbs:detail',kwargs={'id':artical.id}))
# 详情页面
class DetailView(View):
    def get(self,request,id):
        article = ArticleModel.objects.get(pk=id)
        article.read_count+=1
        article.save()
        comments = UserComment.objects.filter(comment_article=article).order_by('add_time')
        i=0
        for comment in comments:
            i+=1
            comment.floor=i
        pagenum = request.GET.get('pagenum', '')
        # 实例化对象，每页4个，在这里可以知道有多少页了
        pa = Paginator(comments, 5)
        try:
            pages = pa.page(pagenum)  # 取前台传过来的页数，如果不是整数或有效对象时抛出异常
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            pages = pa.page(1)
            print("pages2=", pages)

        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            pages = pa.page(pa.num_pages)
            print("pages3=", pages)
        context={
            'article':article,
            'pages':pages
        }
        return render(request,'bbs/show.html',context=context)
# 类的写法
@method_decorator(login_decorator,name='dispatch',)
# @login_decorator
class ReplyView(View):
    def get(self,request):
        article_id = request.GET.get('article_id')
        print("====article_id")

        artcle = ArticleModel.objects.get(pk=article_id)
        context = {
            'article':artcle
        }
        return render(request,'bbs/reply.html',context)
    def post(self,request):

        user_id = request.user.id
        article_id = request.GET.get('article_id')
        comment_content =  request.POST.get('comment_content')
        if user_id is None:
            print("===1=")
            return redirect(reverse('users:user_login'))
        try:
            print("===2=")
            article = ArticleModel.objects.get(pk=article_id)
        except ArticleModel.DoesNotExist:
            print("====")
            return render(request,'bbs/reply.html',context={
                'errmsg':'参数错误'
            })
        print("===3=")
        comment = UserComment.objects.create(
            comment_content = comment_content,
            comment_article=article,
            comment_man_id = user_id
        )
        comment.save()
        return redirect(reverse('bbs:detail', kwargs={'id': article_id}))