from django.contrib import admin
from django.urls import path, include
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('stip/', include('chat.api.urls')),
    path('roomList/', views.room_list, name='room_list'),
    path('room/<str:room_name>/', views.room_messages, name='room_messages'),

]