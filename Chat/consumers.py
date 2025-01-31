import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from Users.models import Customer
from .models import ClassChannel, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_id = self.scope['url_route']['kwargs']['channel_id']
        self.channel_group_name = f'chat_{self.channel_id}'
        
        # Join channel group
        await self.channel_layer.group_add(
            self.channel_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave channel group
        await self.channel_layer.group_discard(
            self.channel_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        
        # Save message to database
        saved_message = await self.save_message(message)
        
        # Send message to channel group
        await self.channel_layer.group_send(
            self.channel_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': saved_message.sender.username,
                'timestamp': saved_message.timestamp.isoformat()
            }
        )
    
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
            'timestamp': event['timestamp']
        }))
        

    
    @database_sync_to_async
    def save_message(self, message):
        channel = ClassChannel.objects.get(id=self.channel_id)
        sender = Customer.objects.get(username=self.scope['user'].username)
        return Message.objects.create(
            channel=channel,
            sender=sender,
            content=message
        )