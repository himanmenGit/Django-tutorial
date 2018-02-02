from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from polls.models import Question


def index(request):
    # 가장 최근에 발행이된(최대 5개) Question목록
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }

    # 쉼표단위로 구분된 Question목록의 각 항목의 question_text로 만들어진 문자열
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def polls(request, question_id):
    return HttpResponse("너는 Polls를 보고 있따.")