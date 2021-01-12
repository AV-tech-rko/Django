from django.contrib import admin
from django.urls import path
from . import views





urlpatterns = [
    
    path('ratings/',views.index,name="list"),
    path('update_task/<str:pk>/',views.updateTask,name="update_task")
]

