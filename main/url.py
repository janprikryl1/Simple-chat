from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('upload_msg/', views.upload, name='upload_msg'),
    path('load/', views.load, name='load'),
    path('l/', views.l, name='l'),
]
