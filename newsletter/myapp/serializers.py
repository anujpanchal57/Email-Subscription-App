from rest_framework import serializers
from pprint import pprint
from .models import Subscriptions

class SubscriptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ('id', "email")