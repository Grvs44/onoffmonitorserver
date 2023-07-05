from rest_framework.serializers import ModelSerializer

from . import models

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = models.Device
        fields = ['id', 'name']


class StatusSerializer(ModelSerializer):
    class Meta:
        model = models.Status
        fields = ['id', 'device', 'status', 'time']
