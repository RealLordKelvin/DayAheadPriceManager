from django.urls import path

from . import views


print('urls')
urlpatterns = [
    path('', views.LoginView, name='register'),
    path('home/', views.LoginView, name='homepage'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name ='login'),
    path('login_suc_page/', views.graph, name ='login_suc_page')
    
]