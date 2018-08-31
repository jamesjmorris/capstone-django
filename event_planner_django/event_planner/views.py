from rest_framework import generics

from .models import Event, Donation
from .serializers import EventSerializer, DonationSerializer

# Create your views here.
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class DonationList(generics.ListCreateAPIView):
    queryset = Donation.objects.all().prefetch_related('event')
    serializer_class = DonationSerializer

class DonationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all().prefetch_related('event')
    serializer_class = DonationSerializer