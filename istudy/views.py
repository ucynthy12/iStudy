
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect,JsonResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import status
from rest_framework.decorators import api_view
from . serializers import *
from rest_framework.authtoken.models import Token





# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data['email']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('customsignup')
  
    else:
        form = SignUpForm()
    return render(request,'registration/registration_form.html',{'form': form})


def customSignup(request):
    customuser=request.user
    if request.method =='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            usercustom=form.save(commit=False)
            usercustom.user = customuser
            usercustom.save()
            return redirect('index')
    
    else:
        form = CustomUserForm()
    return render(request,'registration/customregister_form.html',{'form': form})


class customuserList(APIView):

    def get(self,request):
        custom = CustomUser.objects.all()
        serializer= CustomUserSerializer(custom,many=True)

        return Response(serializer.data)

class usersList(APIView):

    def get(self,request):
        users = User.objects.all()
        serializer= UserSerializer(users,many=True)

        return Response(serializer.data)

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':

        serializer = RegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered a new user.'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token

        else:
            data = serializer.errors
            print(data)
        return Response(data)

def courses_view(request):
    all_Courses = Courses.objects.all()
    print("all_Courses")
    return render(request,'home_for_students.html')

# @api_view(['POST',])
# def custom_registration_view(request):

#     if request.method == 'POST':

#         serializer = CustomSerialiser(data=request.data)
#         data = {}

#         if serializer.is_valid():
#             user = serializer.save()
#             data['role'] = user.role
#             data['phone_number'] = user.phone_number
#             data['full_name'] = user.full_name


#         else:
#             data = serializer.errors
#         return Response(data)

