from django.db import models

class ChatRoom(models.Model):
    
    name = models.TextField(max_length=40, blank=True, null=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Message: {self.content} (Room: {self.room.name})"
