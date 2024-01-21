from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.loginConfirm, name='loginConfirm'),
    path('mypage', views.myPage, name='myPage')
]
