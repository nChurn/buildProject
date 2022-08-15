from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from forms import serializers, models


class BackCallCreateView(generics.CreateAPIView):
    serializer_class = serializers.BackCallCreateSerializer
