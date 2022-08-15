from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from layouts import serializers, models, filters


class LayoutListView(generics.ListAPIView):
    queryset = models.Layout.objects.all()
    serializer_class = serializers.LayoutListSerializer

    filterset_class = filters.LayoutFilter


class LayoutDetailView(generics.RetrieveAPIView):
    queryset = models.Layout
    serializer_class = serializers.LayoutDetailSerializer
