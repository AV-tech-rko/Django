from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('upcominggames/',views.upgames,name="upgames")
]
