# Create your models here.
from django.db import models
from Users.models import Customer

class ClassChannel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='managed_channels')

class Message(models.Model):
    channel = models.ForeignKey(ClassChannel, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']

class ChannelMembership(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    channel = models.ForeignKey(ClassChannel, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'channel')