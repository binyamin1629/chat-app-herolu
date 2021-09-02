from django.db import models
from accounts.models import Account
from chatroom.models import ChatRoom
# Create your models here.

class MessageManager(models.Manager):
    def createMessage(self,subject,message,sent_by,received_by,room_id):
        single_message=self.model(
            subject=subject,
            message=message,
            sent_by=sent_by,
            received_by=received_by,
            room_id=room_id

        )
        single_message.save(using=self._db)
        return single_message


class Message(models.Model):
    subject                =models.CharField(max_length=200)
    message                =models.TextField()  
    createdAt              =models.DateField(auto_now_add=True)
    is_readed_by_receiver  =models.BooleanField(default=False)
    sent_by                =models.ForeignKey(Account,related_name='sent_by',on_delete=models.CASCADE,null=True)
    received_by            =models.ForeignKey(Account,related_name='received_by',on_delete=models.CASCADE,null=True)
    room_id                =models.ForeignKey(ChatRoom,on_delete=models.CASCADE,null=True)
    objects                =MessageManager()


    def __str__(self):
        return self.subject