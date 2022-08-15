from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from floors import serializers, models, filters


class FloorDetailView(generics.RetrieveAPIView):
    queryset = models.Floor.objects.all()
    serializer_class = serializers.FloorSerializer


class FloorListView(generics.ListAPIView):
    queryset = models.Floor.objects.all()
    serializer_class = serializers.FloorSerializer

    filterset_class = filters.FloorFilter
    ordering_fields = ["number"]
