# campaigns/serializers.py
from rest_framework import serializers
from .models import EmailCampaign

class EmailCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCampaign
        fields = ['id', 'name', 'subject', 'content', 'recipients', 'status', 'sent_at']
        read_only_fields = ['status', 'sent_at']