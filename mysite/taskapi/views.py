from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task



# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    ejemplo = {
        "id":"Hola chicos desde Django!!",
        "name":"Fiorella Montes"
    }
    return Response(ejemplo)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)