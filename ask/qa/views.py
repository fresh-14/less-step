from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

from .models import Question
from .utils import get_question_list
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm


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
            answer.author = request.user
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
            question = question_form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect(question)
    else:
        question_form = AskForm()
    return render(request, 'ask.html', {'form': question_form})


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            # Create a new user profile
            new_user = signup_form.save(commit=False)
            new_user.set_password(signup_form.cleaned_data['password'])
            new_user.save()
            # Do auto login user
            login(request, new_user)
            return redirect('qa:main')
    else:
        signup_form = SignUpForm()
    return render(request, 'signup.html', {'form': signup_form})


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request,
                                username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('qa:main')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'form': login_form})


def user_logout(request):
    logout(request)
    return redirect('qa:main')


def test(request, *args, **kwargs):
    return HttpResponse('OK')
