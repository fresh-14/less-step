from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Question
from .utils import get_question_list
from .forms import AskForm, AnswerForm


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
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect(question)
    else:
        answer_form = AnswerForm()
    return render(request, 'detail.html', {'question': question,
                                           'form': answer_form})


def create_question(request):
    if request.method == 'POST':
        question_form = AskForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return redirect(question)
    else:
        question_form = AskForm()
    return render(request, 'ask.html', {'form': question_form})


def test(request, *args, **kwargs):
    return HttpResponse('OK')
