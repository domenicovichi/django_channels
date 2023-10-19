from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

from .models import ChatRoom,Message

def room_list(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat/room_list.html', {'chat_rooms': chat_rooms})

def room_messages(request, room_name):
    chat_room = ChatRoom.objects.get(name=room_name)
    messages = Message.objects.filter(room=chat_room)
    return render(request, 'chat/room_messages.html',{'room_name': room_name, 'messages': messages})