from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from sections import serializers, models, filters


class SectionDetailView(generics.RetrieveAPIView):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer


class SectionListView(generics.ListAPIView):
    queryset = models.Section.objects.all().order_by("building__openDate")
    serializer_class = serializers.SectionSerializer
    filterset_class = filters.SectionFilter
