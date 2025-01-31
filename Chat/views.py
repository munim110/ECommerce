from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ClassChannel, Message, ChannelMembership

# Redirect to login page if user is not authenticated
@login_required(login_url='/users/signin/')
def channel_list(request):
    # Show channels user is a member of or can join
    user_channels = ChannelMembership.objects.filter(user=request.user)
    available_channels = ClassChannel.objects.exclude(
        id__in=user_channels.values_list('channel_id', flat=True)
    )
    
    return render(request, 'channel_list.html', {
        'user_channels': user_channels,
        'available_channels': available_channels
    })

@login_required(login_url='/users/signin/')
def join_channel(request, channel_id):
    channel = get_object_or_404(ClassChannel, id=channel_id)
    
    # Prevent duplicate memberships
    ChannelMembership.objects.get_or_create(
        user=request.user, 
        channel=channel
    )
    
    return redirect('chat', channel_id=channel.id)

@login_required(login_url='/users/signin/')
def chat(request, channel_id):
    channel = get_object_or_404(ClassChannel, id=channel_id)
    
    # Check if user is a member
    membership = ChannelMembership.objects.filter(
        user=request.user, 
        channel=channel
    ).exists()
    
    if not membership:
        return redirect('channel_list')
    
    # Get recent messages
    messages = Message.objects.filter(channel=channel).order_by('-timestamp')[:50]
    
    return render(request, 'chat.html', {
        'channel': channel,
        'messages': messages
    })