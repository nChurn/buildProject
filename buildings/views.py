from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from buildings import serializers, models, filters


class BuildingListView(generics.ListAPIView):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    filterset_class = filters.BuildingFilter


class BuildingDetailView(generics.RetrieveAPIView):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
