from django.urls import path
from . import views

urlpatterns = [
    path('chatrooms/',views.ChatRoomAPIView.as_view(), name = "chatroom-list"),
    path('chatrooms/<int:pk>/',views.ChatRoomDetailAPIView.as_view(), name = "chatroom-detail"),
]