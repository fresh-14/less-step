from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question
from .utils import get_question_list


def new_questions(request):
    qs = Question.objects.new()
    questions = get_question_list(request, qs)
    return render(request, 'list.html', {'questions': questions})


def popular_list_questions(request):
    qs = Question.objects.popular()
    questions = get_question_list(request, qs)
    return render(request, 'list.html', {'questions': questions})


def question_detail(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'detail.html', {'question': question})


def test(request, *args, **kwargs):
    return HttpResponse('OK')
