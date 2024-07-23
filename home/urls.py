from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home',views.index2,name='index2'),
    path('menu', views.menu, name='menu'),
    path('about', views.about, name='about'),]
