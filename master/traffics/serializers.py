from rest_framework import serializers
from .models import TrafficData, TrafficTimeStamp


class TrafficDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficData
        fields = '__all__'


class TrafficTimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficTimeStamp
        fields = '__all__'
