from django_filters import rest_framework as filters

from layouts import models


class LayoutFilter(filters.FilterSet):
    withAvailableObjects = filters.BooleanFilter(method="filter_withAvailableObjects")
    spaceFrom = filters.NumberFilter(field_name="space", lookup_expr="gte")
    spaceTo = filters.NumberFilter(field_name="space", lookup_expr="lte")
    district = filters.CharFilter(field_name="projectId.district")
    openDate = filters.DateFilter(field_name="buildingId.openDate")

    class Meta:
        fields = [
            "projectId",
            "buildingId",
            "sectionId",
            "category",
            "layoutType",
        ]
        model = models.Layout

    def filter_withAvailableObjects(self, queryset, name, value):
        if value:
            return queryset.filter(buildingId__object__status="available").distinct(
                "id"
            )
        return queryset.exclude(buildingId__object__status="available").distinct("id")
