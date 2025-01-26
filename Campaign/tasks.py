from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailCampaign
import json

@shared_task(bind=True)
def send_bulk_emails(self, campaign_id):
    campaign = EmailCampaign.objects.get(id=campaign_id)
    
    try:
        # Parse recipients (assuming JSON list of emails)
        recipients = json.loads(campaign.recipients)
        
        for email in recipients:
            send_mail(
                campaign.subject,
                campaign.content,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        
        campaign.status = 'completed'
        campaign.save()
    except Exception as exc:
        campaign.status = 'failed'
        campaign.save()
        raise self.retry(exc=exc)