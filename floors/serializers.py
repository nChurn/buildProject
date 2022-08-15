from rest_framework import serializers

from floors import models


class FloorSerializer(serializers.ModelSerializer):
    availableObjectsCount = serializers.SerializerMethodField()
    layoutTypes = serializers.SerializerMethodField()

    class Meta:
        fields = [
            "id",
            "projectId",
            "buildingId",
            "sectionId",
            "number",
            "schemeImage",
            "polygonData",
            "availableObjectsCount",
            "layoutTypes",
        ]
        model = models.Floor
