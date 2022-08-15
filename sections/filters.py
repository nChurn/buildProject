from django_filters import rest_framework as filters

from sections import models

from utils.filters import NumberInFilter


class SectionFilter(filters.FilterSet):
    buildingId = filters.NumberFilter(method="filter_buildingId")
    withAvailableObjects = filters.BooleanFilter(method="filter_withAvailableObjects")

    class Meta:
        model = models.Section
        fields = []

    def filter_buildingId(self, queryset, name, value):
        return queryset.filter(building__id=value)

    def filter_withAvailableObjects(self, queryset, name, value):
        if value:
            return queryset.filter(building__object__status="available").distinct("id")
        return queryset.exclude(building__object__status="available").distinct("id")
