from django.shortcuts import render
from .models import PoetInfo
from poem.models import Poem
from operations.models import UserLove
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from tools.decorators import login_decorator
# Create your views here.
def poet_list(request):
    all_poet=PoetInfo.objects.all()
    print("=======image",all_poet[58].image)
    #按朝代排序--诗人排行榜
    # sort_poet=all_poet.order_by('address')[:2]
    # 全局搜索功能的过滤
    keyword = request.GET.get('keyword', '')
    if keyword:
        all_poet = all_poet.filter(name__icontains=keyword)
    #按朝代排序--全部
    sort = request.GET.get('sort','')
    print("排序规则",sort)
    if sort=='address':
        all_poet=all_poet.order_by(sort)
    if sort=='love_num':
        all_poet=all_poet.order_by('-'+sort)
    # 分页
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_poet,30)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request,'poet/poet-list.html',{
        'all_poet':all_poet,
        'pages':pages,
        'sort':sort,
        'keyword':keyword
    })

# 作者详情
@login_decorator
def poet_detail(request,poet_id):
    if poet_id:
        poet = PoetInfo.objects.filter(id=poet_id)[0]
        poem_list = Poem.objects.filter(poetinfo_id=poet_id)
        print("===========")
        print(poem_list)
        # 在返回页面数据的时候，需要返回收藏这首诗的页面是显示收藏还是取消收藏
        lovestatus = False
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=int(poet_id), love_type=3, love_status=True)
            if love:
                lovestatus = True
        return  render(request,'poet/poet-detail.html',{
            'poet':poet,
            'poem_list':poem_list,
            'lovestatus':lovestatus
        })
