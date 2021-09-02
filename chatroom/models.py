from django.db import models
from accounts.models import Account
# Create your models here.

class ChatRoomManager(models.Manager):
    def create_chat_room(self,owner,receiver,room_name):
        chatroom=self.model(
            owner=owner,
            receiver=receiver,
            room_name=room_name
        )
        chatroom.save(using=self._db)
        return chatroom



class ChatRoom(models.Model):
    owner    =models.ForeignKey(Account,related_name='owner',on_delete=models.CASCADE,null=True)
    receiver =models.ForeignKey(Account,related_name='receiver',on_delete=models.CASCADE,null=True)
    room_name=models.CharField(max_length=100)
    objects      =ChatRoomManager()
    
    

    def __str__(self):
        #self.room_name=self.receiver
        return self.room_name

