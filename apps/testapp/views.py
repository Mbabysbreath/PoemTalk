from django.shortcuts import render
# from .models import PoemTest,PoemInfo,PoetInfo
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import render
from django.views.generic.base import View
from .models import PaperList,Question,Paper
from users.models import UserProfile
from operations.models import UserAnswerLog,PaperCache,UserRecord
from datetime import datetime
import random
from django.db.models import Q

# Create your views here.

def po_test(request):
    return render(request, 'testapp/po-test.html')

class PaperListView(View):
    """试题列表页面"""
    def get(self, request):
        papers = PaperList.objects.filter(is_allow=True)
        for i in papers:
            print (i.name, '**', i.id)
        return render(request, "testapp/paper-list.html",
                      {"papers": papers,
                       "title": u"试题列表页面"})

class PaperView(View):
    """试卷页"""
    def get(self, request, paper_id):
        if request.user.is_authenticated:
            print("======1")
            papers_list = PaperList.objects.filter(id=paper_id)
            print("=====2")
            print(papers_list)
            print("====3")

            for papers_list in papers_list:
                papers_list = papers_list
                print("===4")
                print(papers_list.single_choice_num)
            single_choice_score1 = papers_list.single_choice_num*papers_list.single_choice_score
            print("==single_choice_score1==")
            print(single_choice_score1)
            print(papers_list.single_choice_num)
            print(papers_list.single_choice_score)
            judgment_score1 = papers_list.judgment*papers_list.judgment_score
            # multiple_choice_score1 = papers_list.multiple_choice_num*papers_list.multiple_choice_score
            #随机试卷
            if papers_list.random_paper == 1:
                question_list = []
                xz_num = Question.objects.filter(questionType ='xz').count()
                print("==xz==:")
                print(xz_num)
                pd_num = Question.objects.filter(questionType = 'pd').count()
                print("==pd==:")
                print(pd_num)
                #列表解析式写法，将一个列表转换 另一个列表,[)
                seq1 = [i for i in range(1, xz_num+1)]
                print("====================zm=====")
                print(seq1)
                seq2 = [i for i in range(xz_num+1, xz_num+pd_num+1)]
                print("====================zm-1=====")
                print(seq2)
                print("====================zm-2=====")
                print(len(seq1))
                print(papers_list.single_choice_num)
                # question_id_list1 = random.sample(seq1, papers_list.single_choice_num)
                question_id_list1 = random.sample(seq1, len(seq1))
                # question_id_list2 = random.sample(seq2, papers_list.judgment)
                question_id_list2 = random.sample(seq2, len(seq2))
                print(question_id_list1)
                print(question_id_list2)

                # print(len(seq1), len(seq2), len(seq3))
                print("==========zm-4===================")
                print(papers_list.single_choice_num)
                print(papers_list.judgment)
                #extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
                question_id_list1.extend(question_id_list2)
                # question_id_list1.extend(question_id_list3)
                print(question_id_list1)
                for question_id in question_id_list1:

                    question = Question.objects.get(id=question_id)
                    print("====question:")
                    print(question)
                    question_list.append(question)
                    Paper_Cache = PaperCache()
                    Paper_Cache.question = question_id
                    Paper_Cache.user = request.user
                    Paper_Cache.add_time = datetime.now()
                    Paper_Cache.save()
                print('get 方法里用户获取的题目编号为', question_id_list1)  # 显示当前题目编号列表
                question_now = tuple(question_list)  # 题目元组
                print('======题目元组====')
                print(question_now)
                return render(request, "testapp/paper.html", {
                    "question": question_now,
                    "papers_list":papers_list,
                     "single_choice_score":single_choice_score1,
                     "judgment_score":judgment_score1,

                    })
            #固定试卷
            else:
                questions_all = Paper.objects.filter(paper_name_id=paper_id)  # 找到所有试题
                question_list = []
                question_id_list = []
                for questions_ in questions_all:
                    print('paper is ', questions_)
                    question = Question.objects.get(pk=questions_.question_id)
                    question_list.append(question)
                    question_id_list.append(question.id)
                print('get 方法里用户获取的题目编号为', question_id_list)  # 显示当前题目编号列表
                question_now = tuple(question_list)  # 题目元组
                return render(request, "paper.html", {"question": question_now,"papers_list":papers_list,
                                                      "single_choice_score":single_choice_score1, "judgment_score":judgment_score1
                                                      }
                                                      )
        else:
            return render(request, "login.html", {"msg": u'为保证考试客观公正，考题不对未登录用户开放'})

    def post(self, request, paper_id):
        global paper
        #获取刚才答的试卷
        papers_list = PaperList.objects.filter(id=paper_id)
        for papers_list in papers_list:
            papers_list = papers_list
        #随机试卷
        if papers_list.random_paper == 1:
            question_id_lists = PaperCache.objects.filter(user=request.user)
            question_id_list = []
            for question_id in question_id_lists:
                question = Question.objects.get(pk=question_id.question)
                print("======错题")
                print(question)
                question_id_list.append(question.id)
            title = papers_list.name
            print("===title:")
            print(title)
            # 分数记录
            user_score = UserAnswerLog()
            print("====user_score")
            print(user_score)
            # 记录用户
            user_score.user = request.user
            print("====user_score.user")
            print(user_score.user)
            # 记录做题时间
            user_score.add_time = datetime.now()
            temp_score = 0
            #试卷
            user_score.paper_id = papers_list.id
            user_score.paper_name=papers_list.name
            #课程
            user_score.course_id = papers_list.course_id
            wrong_question = []
            user_answer=[]
            for i in question_id_list:
                # 根据编号找到用户提交的对应题号的答案
                user_ans = request.POST.get(str(i), "")

                print(u'试题', i, u'收到的答案是', user_ans)
                # 获取题号为 i 的题目元组对象
                temp_question = Question.objects.get(pk=i)
                # 把正确答案与提交的答案比较
                if temp_question.questionType == 'xz':
                    temp_question.user_ans = user_ans
                    if temp_question.answer == user_ans:
                        temp_score += papers_list.single_choice_score
                        print("试题", temp_question.id, "答案正确")
                    else:
                        question = Question.objects.get(pk=i)
                        question.user_ans=user_ans
                        wrong_question.append(question)

                elif temp_question.questionType == 'pd':
                    if user_ans == "True":
                        user_ans = "对"
                    else:
                        user_ans = '错'
                    temp_question.user_ans = user_ans
                    print(temp_question.answer)

                    if temp_question.answer == user_ans:
                        temp_score += papers_list.judgment_score
                        print("试题", temp_question.id, "答案正确")
                    else:
                        question = Question.objects.get(pk=i)
                        question.user_ans = user_ans
                        wrong_question.append(question)


            wrong_question_now = tuple(wrong_question)
            wrong_question_count = len(wrong_question_now)
            user_score.score = temp_score
            user_score.save()
            question_id_lists.delete()
            return render(request, "testapp/score.html",
                          {"score": user_score.score,
                           "title": title,
                           "wrong_question": wrong_question_now,
                           "wrong_question_count": wrong_question_count,
                           "user_answer":user_answer
                           })



