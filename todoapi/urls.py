from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoItems),
    path('delete/<int:pk>', views.deleteTodoItem),
    path('update/<int:pk>', views.updateTodoItem),
]