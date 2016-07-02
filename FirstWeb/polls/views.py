from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Question, Choice

# Create your views here.
def index(request):
    lastest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list':lastest_question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # 설문투표 폼을 다시 보여줌
        return  render(request, 'polls/detail.html',{'question':p, 'error_message':"답변을 선택하지 않았습니다."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리시 HttpResponsRedirect를 반환하여 리다이렉션 처리
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))