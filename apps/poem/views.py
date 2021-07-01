from django.shortcuts import render
from .models import Poem,PoemType
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from operations.models import UserLove,UserPoem
from django.db.models import Q
from tools.decorators import login_decorator
# Create your views here.
def poem_list(request):
    all_poemtype=PoemType.objects.all()
    keyword = request.GET.get('keyword', '')
    if keyword:
        all_poemtype = all_poemtype.filter(Q(name__icontains=keyword) | Q(detail__icontains=keyword))
    #按照点击量对学习最多的诗词排序，为之后点击进入某一类诗词后，具体诗词做准备
    sort=request.GET.get('sort','')
    if sort:
        print("====sort",sort)
        # sort 升序 -sort降序
        all_poemtype=all_poemtype.order_by('-'+sort)
    # 分页
    pagenum=request.GET.get('pagenum','')
    print("pagenum=",pagenum)
    print("pagenumtype=",type(pagenum))
    #实例化对象，每页4个，在这里可以知道有多少页了
    pa=Paginator(all_poemtype,4)
    try:
        print("=====pages1======")
        pages=pa.page(pagenum) #取前台传过来的页数，如果不是整数或有效对象时抛出异常
        print("pages1=",pages)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        pages=pa.page(1)
        print("pages2=",pages)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pages=pa.page(pa.num_pages)
        print("pages3=",pages)


    return render(request,'poem/poem-list.html',{
        'all_poemtype':all_poemtype,
        'pages':pages,
        'sort':sort,
        'keyword':keyword
    })

# 诗词详情页面poemtype_id
def poem_detail(request,poem_id):
    if poem_id:
        poem = PoemType.objects.filter(id=int(poem_id))[0]
        #学习本类诗词的人数加一
        poem.study_num += 1
        poem.save()
        poem_num = Poem.objects.filter(poemtype_id=int(poem_id))
        # relate_poem=poem
        return render(request,'poem/poem-detail.html',{
            'poem':poem,
            'poem_num':poem_num
        })

# 开始学习诗词-列出种类下所有诗词
def poem_study(request,poemtype_id):
    poemtype=PoemType.objects.filter(id=int(poemtype_id))[0]
    poem = Poem.objects.filter(poemtype_id=int(poemtype_id))
    # 分页
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(poem, 25)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request, 'poem/poem-study.html', {
        'poemtype':poemtype,
        'poem': poem,
        'pages': pages,
        # 'keyword':keyword
    })

#诗词内容
# @login_required(login_url='/users/user_login')
@login_decorator
# @login_decorator
def poem_content(request,poem_id):
    if poem_id:
        poem = Poem.objects.filter(id=int(poem_id))[0]
        poem_type=PoemType.objects.filter(id=int(poem.poemtype_id))[0]
        poem.click_num+=1
        poem.save()
        # 添加用户学习记录,如果没有要添加记录
        userpoem_list = UserPoem.objects.filter(study_man=request.user,study_poem=poem)
        if not  userpoem_list:
            a = UserPoem()
            a.study_man = request.user
            a.study_poem = poem
            a.save()
            poem.study_num += 1
            poem_type.study_num += 1
            poem.save()
            poem_type.save()
    # 在返回页面数据的时候，需要返回收藏这首诗的页面是显示收藏还是取消收藏
        lovestatus=False
        lovepoem=False
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user,love_id=int(poem_id),love_type=2,love_status=True)
            if love:
                lovestatus=True
        print("====lovestatus===")
        print(lovestatus)
        return render(request,'poem/poem-content.html',{
            'poem':poem,
            'lovestatus':lovestatus,
            'poem_type':poem_type
    })

def poem_comment(request,poem_id):
    print("++++++poemid===评论1:", poem_id)
    if poem_id:
        print("++++++poemid===评论2:", poem_id)
        poem = Poem.objects.filter(id = int(poem_id))[0]
        # 切片
        all_comments = poem.usercomment_set.all()[:10]

        print("all_comments===",all_comments,poem)


        return render(request,'poem/poem-comment.html',{
            'poem':poem,
            'all_comments':all_comments,
            # 'poem_list':poem_list
        })

#诗词的全局搜索
def poem_search(request):
    all_poem = Poem.objects.all()
    keyword = request.GET.get('keyword', '')
    no_result = "抱歉，没有搜索您要查找的内容，换个关键词试试吧~"
    if keyword:
        all_poem = all_poem.filter(Q(name__icontains=keyword) | Q(contents__icontains=keyword))
        if not all_poem:
            return render(request, 'poem/poem-search.html', {
                'all_poem': all_poem,
                'keyword': keyword,
                'no_result':no_result
            })
        # 分页
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_poem, 5)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request,'poem/poem-search.html',{
        'all_poem':all_poem,
        'keyword':keyword,
        'pages':pages
    })

