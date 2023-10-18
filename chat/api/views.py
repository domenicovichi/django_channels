from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from chat.models import ChatRoom, Message
from rest_framework import status
from chat.api.serializers import ChatRoomSerializer, MessageSerializer
from rest_framework.response import Response

class ChatRoomAPIView(APIView):
    def get(self,request):
        queryset = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(queryset, many=True)
        return Response(serializer.data)

class ChatRoomDetailAPIView(APIView):
    def get_object(self,pk):
        chatroom = get_object_or_404(ChatRoom, pk=pk)
        return chatroom
    
    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = ChatRoomSerializer(queryset)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ChatRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageAPIView(APIView):
    def get(self,request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)
    
class MessageDetailAPIView(APIView):
    def get_object(self,pk):
        message = get_object_or_404(Message, pk=pk)
        return message
    
    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = MessageSerializer(queryset)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)