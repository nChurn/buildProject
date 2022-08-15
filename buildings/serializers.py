from rest_framework import serializers
from django.db.models import Min, Max, Count
from . import models
from layouts.models import Layout


class BuildingSerializer(serializers.ModelSerializer):

    availableObjectsCount = serializers.SerializerMethodField()
    hasLarder = serializers.SerializerMethodField()
    hasParking = serializers.SerializerMethodField()
    projectId = serializers.IntegerField(source="project.id")
    layoutTypes = serializers.SerializerMethodField()

    class Meta:
        fields = [
            "id",
            "projectId",
            "name",
            "status",
            "masterPlanImage",
            "image",
            "openDate",
            "polygonData",
            "availableObjectsCount",
            "hasLarder",
            "hasParking",
            "layoutTypes",
        ]
        model = models.Building

    def get_availableObjectsCount(self, obj):
        return obj.object_set.filter(status="available").count()

    def get_hasLarder(self, obj):
        if obj.object_set.filter(layout__category="larder"):
            return True
        return False

    def get_hasParking(self, obj):
        if obj.object_set.filter(layout__category="parking"):
            return True
        return False

    def get_layoutTypes(self, obj):
        layouts = []
        for _layout in Layout.LAYOUTS:
            layouts.append(
                {
                    "layoutType": _layout[0],
                    "minPrice": obj.project.object_set.filter(
                        status="available", layout__layoutType=_layout[0]
                    ).aggregate(Min("price"))["price__min"],
                    "availableCount": obj.project.object_set.filter(
                        status="available", layout__layoutType=_layout[0]
                    ).count(),
                }
            )
        return layouts
