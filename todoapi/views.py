from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import todoItem
from .serializers import todoSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def app_root(request):
    # get all endpoints
    endpoints = {
        'items':'/todoitems',
        'delete':'/delete/<int:pk>',
        'update':'/update/<int:pk>',
        'batch update':'/update',
        'token':'/token',
        'refresh token':'/token/refresh',
    }
    return Response(endpoints)

@api_view(['GET', 'POST'])
def todoItems(request):
    
    if request.method == 'POST':
        serializer = todoSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    todos = todoItem.objects.all()
    serializer = todoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def updateTodoItem(request, pk):
    todo = todoItem.objects.get(pk=pk)
    serializer = todoSerializer(todo,data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
def deleteTodoItem(request, pk):
    todos = todoItem.objects.all()
    todo_to_delete = todos.filter(pk=pk)
    if todo_to_delete.exists():
        todo_to_delete.delete()
    else:
        return Response(status=404)
    return Response(status=204)

@api_view(['PUT', 'PATCH'])
def batchTodoUpdate(request):
    todo = todoItem.objects.all()
    serializer = todoSerializer(todo, data=request.data, many=True)
    if serializer.is_valid(raise_exception=True):
        # Perform the batch update
        for i in range(len(serializer.validated_data)):
            todo.filter(pk=request.data[i]['id']).update(title=serializer.validated_data[i]['title'], completed=serializer.validated_data[i]['completed'])
        return Response(serializer.data) 
    return Response(serializer.errors, status=400)


