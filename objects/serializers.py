from rest_framework import serializers
from objects import models
from floors.serializers import FloorSerializer
from layouts.serializers import LayoutDetailSerializer


class ObjectDetailSerializer(serializers.ModelSerializer):
    layoutSpace = serializers.DecimalField(
        source="layout.space", max_digits=6, decimal_places=1
    )
    layoutCategory = serializers.CharField(source="layout.category")
    layoutType = serializers.CharField(source="layout.layoutType")
    floorNumber = serializers.IntegerField(source="floor.number")
    buildingName = serializers.CharField(source="building.name")
    projectName = serializers.CharField(source="project.name")
    layout = LayoutDetailSerializer()
    floor = FloorSerializer()

    class Meta:
        model = models.Object
        fields = [
            "id",
            "status",
            "price",
            "meterPrice",
            "number",
            "entrance",
            "openDate",
            "layoutSpace",
            "layoutCategory",
            "layoutType",
            "floorNumber",
            "buildingName",
            "projectName",
            "finishing",
            "layout",
            "floor",
        ]


class ObjectListSerializer(serializers.ModelSerializer):
    layoutSpace = serializers.DecimalField(
        source="layout.space", max_digits=6, decimal_places=1
    )
    layoutCategory = serializers.CharField(source="layout.category")
    layoutType = serializers.CharField(source="layout.layoutType")
    floorNumber = serializers.IntegerField(source="floor.number")
    buildingName = serializers.CharField(source="building.name")
    projectName = serializers.CharField(source="project.name")

    class Meta:
        model = models.Object
        fields = [
            "id",
            "status",
            "price",
            "meterPrice",
            "number",
            "entrance",
            "openDate",
            "layoutSpace",
            "layoutCategory",
            "layoutType",
            "floorNumber",
            "buildingName",
            "projectName",
            "finishing",
        ]
