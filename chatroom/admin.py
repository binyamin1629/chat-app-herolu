from django.contrib import admin
from .models import ChatRoom
# Register your models here.


class AccountManagment(admin.ModelAdmin):

    prepopulated_fields={'room_name':('receiver',)}
    

admin.site.register(ChatRoom,AccountManagment)