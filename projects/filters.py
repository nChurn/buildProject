from django_filters import rest_framework as filters

from projects import models


class ProjectFilter(filters.FilterSet):
    cityId = filters.NumberFilter(field_name="city")
    priceFrom = filters.NumberFilter(
        field_name="building__object__price", lookup_expr="gte"
    )
    priceTo = filters.NumberFilter(
        field_name="building__object__price", lookup_expr="lte"
    )

    class Meta:
        fields = [
            "status",
            "district",
        ]
        model = models.Project
