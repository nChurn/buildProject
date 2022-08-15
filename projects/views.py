from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from projects import serializers, models, filters


class CityListView(generics.ListAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CityListSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectDetailSerializer


class ProjectListView(generics.ListAPIView):
    queryset = models.Project.objects.all()  # .order_by('building__openDate')
    serializer_class = serializers.ProjectListSerializer

    filterset_class = filters.ProjectFilter
