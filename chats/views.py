from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages,auth
from chatroom.models import ChatRoom
from .models import Message
from accounts.models import Account
from django.contrib.auth.decorators import login_required



@csrf_exempt
@login_required(login_url='login')
def send_message(request,pk):

    if request.method=='POST':
        
        body_unicode=request.body.decode('utf-8')
        data=json.loads(body_unicode) 
        room_id=get_room_id(pk)

        if room_id is not None:
            
            subject=data['subject']
            message=data['message']
            new_message=Message.objects.createMessage(subject,message,request.user,room_id.receiver,room_id)
        else:
            return HttpResponse('no chat room avlible!!!')

    
    return HttpResponse('message has been sent!!!')






def get_room_id(pk):
    room_id=None
    try:
        room_id=ChatRoom.objects.get(id=pk)
    except ChatRoom.DoesNotExist:
        room_id=None
    return room_id


@login_required(login_url='login')
def get_one_message(request,chatID,pk):

    room_id=get_room_id(chatID)
    try:
        message=Message.objects.get(room_id=room_id,id=pk)
        if message is not None:
            return HttpResponse(message.subject+' '+message.message)
    except Message.DoesNotExist:
        return HttpResponse('no such message!!!')


    return  HttpResponse('nothing was found!!!')



@login_required(login_url='login')
def delete_message(request,chatID,pk): 
    room_id=get_room_id(chatID)
    try:      
        deleted_message=Message.objects.get(id=pk,room_id=room_id)
        if request.user==room_id.owner or request.user==room_id.receiver:
            deleted_message.delete()
            return HttpResponse('message has been deleted!!!')
        else:
            return HttpResponse('not autuorized')
    except Message.DoesNotExist:
        return HttpResponse('message does not exist!!!')

    return  HttpResponse('nothing was deleted!!!')







@login_required(login_url='login')
def get_all_messages_by_room_id(request,pk):
    chat_message=''
    room_id=get_room_id(pk)
    if room_id is not None:
        #chek if user is part of the room
        if request.user == room_id.owner or request.user==room_id.receiver:
            messages=Message.objects.filter(room_id=room_id)
            for message in messages:
                chat_message+='subject: '+message.subject+' ' +'message: '+message.message+ ' \n'+' '
            #set is_readed_by_receiver to True since the user requested all messages     
            messages=Message.objects.filter(room_id=room_id).update(is_readed_by_receiver=True)
            return HttpResponse('all messages!!!  '+chat_message)
    else:
        return HttpResponse('no messages found')
    return HttpResponse('no messages found your not authorized')



        
@login_required(login_url='login')
def unread_message(request,uid):

    #find user 
    user = Account.objects.get(id=uid)
    if user is not None:
        #all rooms that user is a part of.
        rooms_that_user_is_part_of = ChatRoom.objects.filter(receiver=user)


        #unread_messages=Message.objects.filter(room_id=rooms_that_user_is_part_of,is_readed_by_receiver=False)
        count_of_messages=0
       

        
        
        for rooms in rooms_that_user_is_part_of:          
            mesages=Message.objects.filter(is_readed_by_receiver=False)
            
            for message in mesages:
                count_of_messages=count_of_messages+1

        string_Count=str(count_of_messages)
        return HttpResponse('you have '+string_Count)
            
    else:

        return HttpResponse('no messages found, no such user ')
