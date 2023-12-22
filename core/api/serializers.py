from rest_framework import serializers

from .models import LinkItem, SleepingModePhoto


class LinkItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkItem
        fields = ['pk', 'title', 'link', 'photo']


class SleepingModePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepingModePhoto
        fields = ['pk', 'photo']

