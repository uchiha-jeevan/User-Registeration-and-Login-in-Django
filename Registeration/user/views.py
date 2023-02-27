from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import models
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def signup(request):
    if request.method=='POST':

        if 'username' in request.POST:
            username=request.POST['username']
            email=request.POST['email']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            #print('the values',username,email,pass1)
            if pass1 == pass2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exists')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Username already exists')
                    return redirect('signup')
                else:
                    user=User.objects.create_user(username=username,email=email,password=pass1)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,'password and conform password are not same')
                return redirect('signup')
        else:
            messages.info(request,'enter details')
            return redirect('signup')

    return render(request,'signup.html')

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'home.html',{'name':user.username})
        else:
            messages.info(request,'invalid credintails')
            return redirect('login')


    return render(request,'login.html')
