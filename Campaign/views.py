# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import EmailCampaign
from .serializers import EmailCampaignSerializer
from .tasks import send_bulk_emails

class EmailCampaignViewSet(viewsets.ModelViewSet):
    queryset = EmailCampaign.objects.all()
    serializer_class = EmailCampaignSerializer

    @action(detail=True, methods=['post'])
    def send(self, request, pk=None):
        campaign = self.get_object()
        
        # Trigger async email sending
        send_bulk_emails.delay(campaign.id)
        
        return Response({
            'status': 'Campaign queued for sending',
            'campaign_id': campaign.id
        }, status=status.HTTP_202_ACCEPTED)