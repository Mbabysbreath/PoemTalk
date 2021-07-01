from django.shortcuts import render
from django.views.generic.base import View
from .models import PaperList,Question
from operations.models import UserAnswerLog,PaperCache
from datetime import datetime
import random
# Create your views here.

def po_test(request):
    return render(request, 'exam/po-test.html')
class PaperListView(View):
    """试题列表页面"""
    def get(self, request):
        papers = PaperList.objects.filter(is_allow=True)
        print("======")
        print(papers)
        for i in papers:
            print (i.name, '**', i.id)
        return render(request, "exam/paper-list.html", {"papers": papers, "title": u"试题列表页面"})

class PaperView(View):
    """试卷页"""
    def get(self, request, paper_id):
        if request.user.is_authenticated:
            papers_list = PaperList.objects.filter(id=paper_id)[0]
            single_choice_score1 = papers_list.single_choice_num*papers_list.single_choice_score
            judgment_score1 = papers_list.judgment*papers_list.judgment_score
            #随机试卷
            if papers_list.random_paper == 1:
                question_list = []
                xz_num = Question.objects.filter(questionType ='xz').count()
                pd_num = Question.objects.filter(questionType = 'judgment').count()
                print("==xz==:")
                print(xz_num,pd_num)
                seq1 = [i for i in range(1, xz_num+1)]
                seq2 = [i for i in range(xz_num+1, xz_num+pd_num+1)]
                print("====================zm=====")
                print(seq1,seq2)
                question_id_list1 = random.sample(seq1, papers_list.single_choice_num)
                print("question_id_list1=",question_id_list1)
                question_id_list2 = random.sample(seq2, papers_list.judgment)
                print("question_id_list2=", question_id_list2)
                question_id_list1.extend(question_id_list2)
                print(question_id_list1)
                for question_id in question_id_list1:
                    question = Question.objects.get(id=question_id)
                    question_list.append(question)
                    Paper_Cache = PaperCache()
                    Paper_Cache.question = question_id
                    Paper_Cache.user = request.user
                    Paper_Cache.add_time = datetime.now()
                    Paper_Cache.save()
                print('get 方法里用户获取的题目编号为', question_id_list1)  # 显示当前题目编号列表
                question_now = tuple(question_list)  # 题目元组
                return render(request, "exam/paper.html", {"question": question_now,"papers_list":papers_list,
                                                      "single_choice_score":single_choice_score1, "judgment_score":judgment_score1
                                                      }
                                                      )
        else:
            return render(request, "login.html", {"msg": u'为保证考试客观公正，考题不对未登录用户开放'})

    def post(self, request, paper_id):
        global paper
        #获取刚才答的试卷
        papers_list = PaperList.objects.filter(id=paper_id)[0]
        #随机试卷
        if papers_list.random_paper == 1:
            question_id_lists = PaperCache.objects.filter(user=request.user)
            print("question_lists_id=",question_id_lists)
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
            user_log = UserAnswerLog()
            print("====user_log")
            print(user_log)
            # 记录用户
            user_log.user = request.user
            print("====user_score.user")
            print(user_log.user)
            # 记录做题时间
            user_log.add_time = datetime.now()
            temp_score = 0
            #试卷
            user_log.paper_id = papers_list.id
            user_log.paper_name=papers_list.name
            #课程
            user_log.course_id = papers_list.course_id
            wrong_question = []
            for q_id in question_id_list:
                # 根据编号找到用户提交的对应题号的答案
                user_ans = request.POST.get(str(q_id), "")
                # print(u'试题', q_id, u'用户答案是:', user_ans)
                # 获取题号为 i 的题目元组对象
                temp_question = Question.objects.get(pk=q_id)
                # 把正确答案与提交的答案比较
                if temp_question.questionType == 'xz':
                    temp_question.user_ans = user_ans
                    if temp_question.answer == user_ans:
                        temp_score += papers_list.single_choice_score
                        print("选择题", temp_question.id, temp_question.answer, user_ans, "回答正确")
                    else:
                        print("选择题", temp_question.id, temp_question.answer, user_ans, "回答错误")
                        question = Question.objects.get(pk=q_id)
                        question.user_ans=user_ans
                        wrong_question.append(question)

                elif temp_question.questionType == 'judgment':
                    if user_ans == "True":
                        user_ans = "对"
                    elif user_ans=='False':
                        user_ans = '错'
                    else:
                        user_ans=" "
                    temp_question.user_ans = user_ans
                    if temp_question.answer == user_ans:
                        temp_score += papers_list.judgment_score
                        print("判断题", temp_question.id,temp_question.answer,user_ans, "回答正确")

                    else:
                        print("判断题", temp_question.id, temp_question.answer, user_ans, "回答错误")
                        question = Question.objects.get(pk=q_id)
                        print("类型",question.questionType)
                        question.user_ans = user_ans
                        wrong_question.append(question)
            print("错题集合",wrong_question)


            wrong_question_now = tuple(wrong_question)
            wrong_question_count = len(wrong_question_now)
            wrong_question=[]
            user_log.score = temp_score
            user_log.save()
            question_id_lists.delete()
            return render(request, "exam/score.html",
                          {"score": user_log.score,
                           "title": title,
                           "wrong_question": wrong_question_now,
                           "wrong_question_count": wrong_question_count
                           })




