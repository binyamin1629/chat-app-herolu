from django.urls import path
from . import  views


urlpatterns=[
    path('',views.create_chat_room,name='create_chat_room')
]

