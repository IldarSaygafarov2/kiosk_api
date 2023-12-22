from django.shortcuts import render
from .serializers import LinkItemSerializer, SleepingModePhotoSerializer
from .models import LinkItem, SleepingModePhoto
from rest_framework.generics import ListAPIView


class LinkItemList(ListAPIView):
    queryset = LinkItem.objects.all()
    serializer_class = LinkItemSerializer


class SleepingModePhotoList(ListAPIView):
    queryset = SleepingModePhoto.objects.all()
    serializer_class = SleepingModePhotoSerializer

