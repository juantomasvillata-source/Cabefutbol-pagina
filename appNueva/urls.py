from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.index2, name='inicio2'),    
    path('login/', views.vista_login, name='login'),
    path('signup/', views.vista_signup, name='signup'),
]