from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from main_pages import serializers, models


class CompanyView(generics.ListAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class InvestorView(generics.ListAPIView):
    queryset = models.Investor.objects.all()
    serializer_class = serializers.InvestorSerializer
