from django_filters import rest_framework as filters

from objects import models

from utils.filters import NumberInFilter


class ObjectFilter(filters.FilterSet):
    projectId = filters.NumberFilter(field_name="project__id")
    buildingId = filters.NumberFilter(field_name="building__id")
    sectionId = filters.NumberFilter(field_name="floor__sectionId")
    layoutId = filters.NumberFilter(field_name="layout__id")
    floorId = filters.NumberFilter(field_name="floor__id")
    district = filters.CharFilter(field_name="project__district")
    priceFrom = filters.NumberFilter(field_name="price", lookup_expr="gte")
    priceTo = filters.NumberFilter(field_name="price", lookup_expr="lte")
    spaceFrom = filters.NumberFilter(field_name="layout__space", lookup_expr="gte")
    spaceTo = filters.NumberFilter(field_name="layout__space", lookup_expr="lte")
    category = filters.CharFilter(field_name="layout__category")
    layoutType = filters.CharFilter(field_name="layout__layoutType")
    ids = NumberInFilter(field_name="id", lookup_expr="in")

    class Meta:
        fields = [
            "status",
            "openDate",
        ]
        model = models.Object
