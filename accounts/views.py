from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages,auth
# Create your views here.
@csrf_exempt
def register(request):

    if request.user.is_authenticated:
        return HttpResponse('user is logged in alredy!!!')
    

    if request.method=='POST':
       body_unicode=request.body.decode('utf-8')
       data=json.loads(body_unicode) 
       first_name=data['first_name']
       last_name=data['last_name']
       email=data['email']
       password=data['password']
       username=data['username']


        #add try except block to chek if user alredy extists
       user=Account.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
       user.save()    
    else:
        return  HttpResponse('nice created!!!')    



    return HttpResponse('accounts created!!!')





@csrf_exempt    
def login(request):
    if request.user.is_authenticated:
        return HttpResponse('user is logged in alredy!!!')
    if request.method=='POST':
       body_unicode=request.body.decode('utf-8')
       data=json.loads(body_unicode) 
       email=data['email']
       password=data['password']
       user=auth.authenticate(email=email,password=password) 
       if user is not None:
           auth.login(request,user)
           return HttpResponse('user is logged in!!!')
       else:
            return HttpResponse('wrong email or password please try again')
    else:        
        return HttpResponse('login here')  



def logout(request):

    user=request.user.first_name
    auth.logout(request)
    return HttpResponse('user logged out '+user)

    
