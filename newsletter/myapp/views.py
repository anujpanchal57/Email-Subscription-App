from django.shortcuts import render
from pprint import pprint
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import SubscriptionsSerializer
from .models import Subscriptions
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def subscriptions_list(request):
    if request.method == "GET":
        subscriptions = Subscriptions.objects.all().order_by('email')
        sub_serializer = SubscriptionsSerializer(subscriptions, many=True)
        return JsonResponse(sub_serializer.data, safe=False)
    if request.method == "POST":
        sub_data = JSONParser().parse(request)
        sub_serializer = SubscriptionsSerializer(data=sub_data)
        if sub_serializer.is_valid():
            sub_serializer.save()
            return JsonResponse(sub_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(sub_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

