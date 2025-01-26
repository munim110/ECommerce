from django.db import models

# Create your models here.
from django.db import models

class EmailCampaign(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    recipients = models.TextField()  # CSV or JSON of email addresses
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.name