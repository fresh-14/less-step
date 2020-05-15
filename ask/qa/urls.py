from django.urls import path

from . import views

app_name = 'qa'

urlpatterns = [
    path('new/', views.test, name='new'),
    path('popular/', views.popular_list_questions, name='popular'),
    path('ask/', views.create_question, name='create_question'),
    path('question/<int:id>/', views.question_detail, name='question'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.new_questions, name='main'),
]

