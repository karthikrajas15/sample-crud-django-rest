# Django LIB
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# restframework LIB
from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# Local DIR LIB
from .serializers import *
from .models import Task

# Create your views here.
class UserRegistration(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        data_request = request.data
        serializer = self.get_serializer(data=data_request)
        if serializer.is_valid():
            serializer.save()
            message = "User Registered Successfully"
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            message = "User Registraion Failed."
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class UserLogin(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        data_request = request.data
        serializer = self.get_serializer(data=data_request)
        if serializer.is_valid():
            user = User.objects.filter(email=data_request.get('email')).first()
            token = Token.objects.filter(user=user).first()
            message = "User Loggedin Successfully"
            return Response({'success': True, 'token': token.key}, status=status.HTTP_200_OK)
        else:
            message = "User Login Failed."
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class TaskCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = TaskListSerializer

    def create(self, request, *args, **kwargs):
        data_request = request.data
        serializer = self.get_serializer(data=data_request)
        if serializer.is_valid():
            data = serializer.save(user=request.user)
            s_data = {'title': data.title, 'status': data.status}
            message = "{0} Task Created Successfully".format(data.title)
            return Response({'success': True, 'data': s_data}, status=status.HTTP_201_CREATED)
        else:
            message = "Task Creation Failed."
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class TaskUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def patch(self, request, pk=None, *args, **kwargs):
        question = get_object_or_404(Task, pk=pk)
        serializer = TaskListSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            message = "Task Updated Successfully"
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            message = "Task Creation Failed."
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class TaskDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def destroy(self, request, pk=None,  *args, **kwargs):
        if Task.objects.filter(pk=pk).exists():
            Task.objects.filter(pk=pk).delete()
            message = "Task Deletion Successfully."
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            message = "Task Deletion Failed."
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
