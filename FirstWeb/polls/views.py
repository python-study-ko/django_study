from django.shortcuts import render
from polls.models import Question

# Create your views here.
def index(request):
    lastest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list':lastest_question_list}
    return render(request,'polls/index.html',context)