from django.urls import path
from .views import sendmail

urlpatterns = [
    path("sendmail/", sendmail, name='sendmail')
]
