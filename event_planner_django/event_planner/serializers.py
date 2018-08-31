from rest_framework import serializers
from .models import Event, Donation

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'location', 'date', 'description', 'cost', 'img_url',)

class DonationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donation
        fields = ('id', 'event', 'amount', 'date', 'comment',)