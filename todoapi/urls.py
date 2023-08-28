from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.app_root, name='app_root'),
    path('todoitems', views.todoItems, name='todoItems'),
    path('delete/<int:pk>', views.deleteTodoItem, name='deleteTodoItem'),
    path('update/<int:pk>', views.updateTodoItem, name='updateTodoItem'),
    #path('update', views.batchTodoUpdate, name='batchTodoUpdate'),
    path('token', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]