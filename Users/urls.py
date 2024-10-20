from django.urls import path
from .views import signin, signup


urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
]
