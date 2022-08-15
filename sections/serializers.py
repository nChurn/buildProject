from rest_framework import serializers
from sections import models
from layouts.models import Layout


class SectionSerializer(serializers.ModelSerializer):
    floorsCount = serializers.SerializerMethodField()
    availableObjectsCount = serializers.SerializerMethodField()
    projectId = serializers.IntegerField(source="building.project.id")
    buildingId = serializers.IntegerField(source="building.id")
    layoutTypes = serializers.SerializerMethodField()

    class Meta:
        fields = [
            "id",
            "projectId",
            "buildingId",
            "name",
            "masterPlanImage",
            "polygonData",
            "floorsCount",
            "availableObjectsCount",
            "layoutTypes",
        ]
        model = models.Section

    def get_floorsCount(self, obj):
        return obj.floor_set.count()

    def get_availableObjectsCount(self, obj):
        return obj.building.object_set.count()

    def get_layoutTypes(self, obj):
        layouts = []
        for _layout in Layout.LAYOUTS:
            layouts.append(
                {
                    "layoutType": _layout[0],
                    "minPrice": obj.object_set.filter(
                        status="available", layout__layoutType=_layout[0]
                    ).aggregate(Min("price"))["price__min"],
                    "availableCount": obj.object_set.filter(
                        status="available", layout__layoutType=_layout[0]
                    ).count(),
                }
            )
        return layouts
