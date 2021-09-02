from django.shortcuts import render
from django.http import HttpResponse
from .models import ChatRoom
from django.views.decorators.csrf import csrf_exempt
import json
from accounts.models import Account
from django.contrib.auth.decorators import login_required
# Create your views here.




@csrf_exempt
@login_required(login_url='login')
def create_chat_room(request):


    if request.method=='POST':
       #chek if chat room alredy exsits
       owenr = Account.objects.get(email=request.user.email)      
       
       body_unicode=request.body.decode('utf-8')
       data=json.loads(body_unicode) 
       receivers_email=data['receivers_email']
       room_name=data['room_name']
       try:
           receiver = Account.objects.get(email=receivers_email)
       except Account.DoesNotExist:
           return HttpResponse('no user found!!! ')
       if receiver is not None:
           new_chat_room = ChatRoom.objects.create_chat_room(owenr,receiver,room_name) 
           new_chat_room.save()
           return HttpResponse('chat room was created')
       else:
           return HttpResponse('create your user here')
