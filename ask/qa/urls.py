from django.urls import path
from . import views

app_name = 'qa'

urlpatterns = [
    path('new/', views.test, name='new'),
    path('popular/', views.popular_list_questions, name='popular'),
    path('ask/', views.test, name='ask'),
    path('question/<int:id>/', views.question_detail, name='question'),
    path('signup/', views.test, name='signup'),
    path('login/', views.test, name='login'),
    path('', views.new_questions, name='main'),
]

