from django.conf.urls import url
from django.urls import path

from . import views
from .views import packets, getPacketCount

urlpatterns = [
    path('', packets, name='packet_sniffer_logger'),
    path('get/', getPacketCount, name='get_packet')
]
