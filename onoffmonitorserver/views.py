# pylint:disable=no-member
from django_filters.rest_framework import DjangoFilterBackend
from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from . import models
from .filters import DeviceOwnerFilter, StatusOwnerFilter
from .permissions import IsDeviceOwner, IsStatusOwner
from .serializers import MonitorSerializer, DeviceSerializer, StatusSerializer


class MonitorViewSet(ModelViewSet):
    """
    ViewSet for managing Monitor objects
    """
    queryset = models.Monitor.objects.all()
    serializer_class = MonitorSerializer
    permission_classes = [IsAuthenticated, IsDeviceOwner]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = [DeviceOwnerFilter]


class DeviceViewSet(ModelViewSet):
    """
    ViewSet for managing Device objects
    """
    queryset = models.Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsDeviceOwner]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = [DeviceOwnerFilter, DjangoFilterBackend]
    filterset_fields = ['monitor']


class StatusViewSet(ModelViewSet):
    """
    ViewSet for managing Status objects
    """
    queryset = models.Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated, IsStatusOwner]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = [StatusOwnerFilter]

    @action(methods=['POST'], detail=False, url_path='n')
    def create_no_return(self, request):
        """
        Create a Status object but don't return the created data
        """
        response = super().create(request)
        response.data = None
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
