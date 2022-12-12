from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/',views.abouts,name='about'),
    path('details/',views.details,name='details'),
]

