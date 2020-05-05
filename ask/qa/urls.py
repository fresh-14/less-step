from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.test, name='new'),
    path('popular/', views.test, name='popular'),
    path('ask/', views.test, name='ask'),
    path('question/<int:id>/', views.test, name='question'),
    path('signup/', views.test, name='signup'),
    path('login/', views.test, name='login'),
    path('', views.test, name='main'),
]

