from rest_framework.serializers import ModelSerializer, ValidationError, CurrentUserDefault

from . import models


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = models.Device
        fields = ['id', 'name']


class StatusSerializer(ModelSerializer):
    def validate(self, attrs):
        if attrs['device'].user != CurrentUserDefault():
            raise ValidationError('Device owner must be the current user')
        return super().validate(attrs)

    class Meta:
        model = models.Status
        fields = ['id', 'device', 'status', 'time']
