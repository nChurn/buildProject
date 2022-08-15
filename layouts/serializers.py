from rest_framework import serializers
from layouts import models


class LayoutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LayoutImage
        fields = ["image"]


class LayoutListSerializer(serializers.ModelSerializer):
    images = LayoutImageSerializer(many=True, source="layoutimage_set")
    sectionOpenDate = serializers.DateField(source="sectionId.building.openDate")
    projectName = serializers.CharField(source="projectId.name")
    buildingName = serializers.CharField(source="buildingId.name")
    discount = serializers.CharField(source="projectId.discount")
    minPrice = serializers.SerializerMethodField()
    availableObjectsCount = serializers.SerializerMethodField()
    availableObjectId = serializers.SerializerMethodField()

    class Meta:
        model = models.Layout
        fields = [
            "id",
            "images",
            "projectId",
            "buildingId",
            "sectionId",
            "name",
            "category",
            "layoutType",
            "discount",
            "space",
            "sectionOpenDate",
            "polygonData",
            "projectName",
            "buildingName",
            "minPrice",
            "availableObjectsCount",
            "availableObjectId",
        ]

    def get_minPrice(self, obj):
        return obj.buildingId.object_set.aggregate(Min("price"))["price__min"]

    def get_availableObjectsCount(self, obj):
        return obj.buildingId.object_set.filter(status="available").count()

    def get_availableObjectId(self, obj):
        try:
            return (
                obj.buildingId.object_set.filter(status="available")
                .order_by("price")
                .first()
                .id
            )
        except:
            return


class LayoutDescriptionImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["image"]
        model = models.LayoutDescriptionImage


class LayoutDetailSerializer(serializers.ModelSerializer):
    images = LayoutImageSerializer(many=True, source="layoutimage_set")
    sectionOpenDate = serializers.DateField(source="sectionId.building.openDate")
    projectName = serializers.CharField(source="projectId.name")
    buildingName = serializers.CharField(source="buildingId.name")
    minPrice = serializers.SerializerMethodField()
    sectionFloorsCount = serializers.SerializerMethodField()
    discount = serializers.CharField(source="projectId.discount")
    availableObjectsCount = serializers.SerializerMethodField()
    availableObjectId = serializers.SerializerMethodField()
    projectAddress = serializers.CharField(source="projectId.address")
    projectDistrict = serializers.CharField(source="projectId.district")
    spaceWithBalcony = serializers.SerializerMethodField()
    descriptionImages = LayoutDescriptionImageSerializer(many=True, read_only=True)

    class Meta:
        fields = [
            "id",
            "projectId",
            "buildingId",
            "sectionId",
            "name",
            "category",
            "layoutType",
            "discount",
            "space",
            "sectionOpenDate",
            "polygonData",
            "projectName",
            "buildingName",
            "minPrice",
            "availableObjectsCount",
            "availableObjectId",
            "images",
            "sectionFloorsCount",
            "projectAddress",
            "projectDistrict",
            "balconyCount",
            "livingSpace",
            "spaceWithBalcony",
            "windowsPosition",
            "description",
            "descriptionImages",
        ]
        model = models.Layout

    def get_minPrice(self, obj):
        return obj.buildingId.object_set.aggregate(Min("price"))["price__min"]

    def get_availableObjectsCount(self, obj):
        return obj.buildingId.object_set.filter(status="available").count()

    def get_availableObjectId(self, obj):
        try:
            return (
                obj.buildingId.object_set.filter(status="available")
                .order_by("price")
                .first()
                .id
            )
        except:
            return

    def get_sectionFloorsCount(self, obj):
        obj.floorLayout.floor_set.count()

    def get_spaceWithBalcony(self, obj):
        return obj.livingSpace + obj.balconyCount
