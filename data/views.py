from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from data import serializers, models


class OrganizationView(generics.ListAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class BankListView(generics.ListAPIView):
    queryset = models.Bank.objects.all()
    serializer_class = serializers.BankSerializer
