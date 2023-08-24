from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import todoItem
from .serializers import todoSerializer

@api_view(['GET', 'POST'])
def todoItems(request):
    
    if request.method == 'POST':
        serializer = todoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = todoSerializer(data=request.data)
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

@api_view(['GET'])
def deleteTodoItem(request, pk):
    todo = todoItem.objects.get(pk=pk)
    todo.delete()
    return HttpResponse(status=204)