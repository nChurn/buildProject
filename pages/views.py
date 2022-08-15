from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from pages import serializers, models


class PageDetailView(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageDetailSerializer


class PageListView(generics.ListAPIView):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageListSerializer
