from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from objects import serializers, models, filters


class ObjectDetailView(generics.RetrieveAPIView):
    queryset = models.Object.objects.all()
    serializer_class = serializers.ObjectDetailSerializer


class ObjectListView(generics.ListAPIView):
    queryset = models.Object.objects.all().order_by("price")
    serializer_class = serializers.ObjectListSerializer

    pagination_class = LimitOffsetPagination

    filterset_class = filters.ObjectFilter
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    ordering_fields = [
        "price",
        "space",
        "number",
        "status",
        "layout__layoutType",
        "entrance",
        "floor__number",
        "building__name",
        "project__name",
        "layout__category",
    ]
