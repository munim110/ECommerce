from django.urls import path
from . import views

urlpatterns = [
    path('channels/', views.channel_list, name='channel_list'),
    path('channels/join/<int:channel_id>/', views.join_channel, name='join_channel'),
    path('chat/<int:channel_id>/', views.chat, name='chat'),
]