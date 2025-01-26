from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailCampaignViewSet

router = DefaultRouter()
router.register(r'', EmailCampaignViewSet, basename='campaign')

urlpatterns = [
] + router.urls