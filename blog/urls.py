from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('curiosidades/', views.fatos_list, name='curiosidades'),
    path('curiosidades/<int:pk>/', views.fatos_detail, name='fatos_detail'),

    path('aleatoriedades/', views.aleatorio_list, name='aleatoriedades'),
    path('aleatoriedades/<int:pk>/', views.aleatorio_detail, name='aleatorio_detail'),

] 