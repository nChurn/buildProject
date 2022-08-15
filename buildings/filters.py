from django_filters import rest_framework as filters

from buildings import models


class BuildingFilter(filters.FilterSet):
    projectId = filters.NumberFilter(field_name="project")
    withAvailableObjects = filters.BooleanFilter(method="filter_withAvailableObjects")

    class Meta:
        fields = ["openDate"]
        model = models.Building

    def filter_withAvailableObjects(self, queryset, name, value):
        if value:
            return queryset.filter(object__status="available").distinct("id")
        return queryset.exclude(object__status="available").distinct("id")
