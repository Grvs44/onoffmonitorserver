from rest_framework.serializers import ModelSerializer, ValidationError, CurrentUserDefault, HiddenField

from . import models


class BaseSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())


class MonitorSerializer(BaseSerializer):
    class Meta:
        model = models.Device
        fields = ['id', 'name', 'user']


class DeviceSerializer(BaseSerializer):
    def validate(self, attrs):
        print(attrs)
        if attrs['monitor'].user != attrs['user']:
            raise ValidationError('Device owner must be the current user')
        return super().validate(attrs)

    class Meta:
        model = models.Device
        fields = ['id', 'name', 'user', 'monitor', 'gpio_input', 'gpio_led']


class StatusSerializer(ModelSerializer):
    def validate(self, attrs):
        if attrs['device'].user != attrs['user']:
            raise ValidationError('Device owner must be the current user')
        return super().validate(attrs)

    class Meta:
        model = models.Status
        fields = ['id', 'device', 'status', 'time', 'user']
