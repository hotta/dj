from django.shortcuts import get_object_or_404, render
from django.http      import HttpResponse, Http404
from django.template  import loader

from .models          import Question

# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = { 'latest_question_list': latest_question_list, }
  ''' HttpResponse() を返すやり方
  template = loader.get_template('polls/index.html')
  return HttpResponse(template.render(context, request))
  '''

  # render() ショートカットを使うやり方
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  ''' try ～ except で書くやり方
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotxist:
    raise Http404("Question does not exist.")
  '''

  # get_object_or_404() ショートカットを使うやり方
  question = get_object_or_404(Question, pk=question_id)

  return render(request, "polls/detail.html", { 'question': question })

def results(request, question_id):
  response = "You're looking at the results of question %s"
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
