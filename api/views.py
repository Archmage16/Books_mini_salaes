from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import *

class MessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # сохраняет данные в БД
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def Print_mess(request):
    messages = Message.objects.all()
    
    return render(request, 'messages.html', {'messages': messages})

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully!'}, status=201)
        return Response(serializer.errors, status=400)

def Print_user(request):
    users = User.objects.all()
    
    return render(request, 'user_info.html', {'users': users})