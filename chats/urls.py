from django.urls import path
from . import  views


urlpatterns=[
    path('message/<int:pk>',views.send_message,name='send_message'),
    path('delete-message/chatid/<int:chatID>/<int:pk>',views.delete_message,name='delete_message'),
    path('get-all-messages/<int:pk>',views.get_all_messages_by_room_id,name='get_all_messages'),
    path('get-one-messages/chatid/<int:chatID>/<int:pk>',views.get_one_message,name='get_one_message'),
    path('unread-messages/<int:uid>',views.unread_message,name='unread_message')
]

