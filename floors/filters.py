from django_filters import rest_framework as filters

from floors import models


class FloorFilter(filters.FilterSet):
    withAvailableObjects = filters.BooleanFilter(method="filter_withAvailableObjects")

    class Meta:
        fields = [
            "sectionId",
        ]
        model = models.Floor

    def filter_withAvailableObjects(self, queryset, name, value):
        if value:
            return queryset.filter(object__status="available")
        return queryset.exclude(object__status="available")
