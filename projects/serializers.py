from rest_framework import serializers
from django.db.models import Min, Max

from projects import models


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name", "active"]
        model = models.City


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "image"
        model = models.ProjectImage


class ProjectListSerializer(serializers.ModelSerializer):
    minPrice = serializers.SerializerMethodField()
    openDate = serializers.SerializerMethodField()
    availableObjectsCount = serializers.SerializerMethodField()
    layoutTypes = serializers.SerializerMethodField()

    class Meta:
        fields = [
            "id",
            "name",
            "status",
            "address",
            "minPrice",
            "openDate",
            "mainImage",
            "discount",
            "hasNewBuildings",
            "location",
            "availableObjectsCount",
            "layoutTypes",
        ]
        model = models.Project

    def get_minPrice(self, obj):
        try:
            return obj.object_set.aggregate(Min("price"))["price__min"]
        except:
            return

    def get_openDate(self, obj):
        try:
            return obj.building_set.latest("openDate").openDate
        except:
            return

    def get_availableObjectsCount(self, obj):
        try:
            return obj.object_set.filter(status="available").count()
        except:
            return

    def get_layoutTypes(self, obj):
        layouts = []
        for _layout in models.Layout.LAYOUTS:
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


class ProjectDetailSerializer(serializers.ModelSerializer):
    minPrice = serializers.SerializerMethodField()
    openDate = serializers.SerializerMethodField()
    availableObjectsCount = serializers.SerializerMethodField()
    layoutTypes = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    nearerObjects = serializers.SerializerMethodField()
    projectBenefits = serializers.SerializerMethodField()
    constructionReports = serializers.SerializerMethodField()

    class Meta:
        fields = [
            "id",
            "name",
            "status",
            "minPrice",
            "openDate",
            "mainImage",
            "discount",
            "hasNewBuildings",
            "location",
            "availableObjectsCount",
            "layoutTypes",
            "district",
            "masterPlanImage",
            "description",
            "images",
            "nearerObjects",
            "projectBenefits",
            "constructionReports",
        ]
        model = models.Project

    def get_minPrice(self, obj):
        try:
            return obj.object_set.aggregate(Min("price"))["price__min"]
        except:
            return

    def get_openDate(self, obj):
        try:
            return obj.building_set.latest("openDate").openDate
        except:
            return

    def get_availableObjectsCount(self, obj):
        try:
            return obj.object_set.filter(status="available").count()
        except:
            return

    def get_layoutTypes(self, obj):
        layouts = []
        for _layout in models.Layout.LAYOUTS:
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

    def get_images(self, obj):
        images = [image.image.name for image in obj.projectimage_set.all()]
        return images

    def get_nearerObjects(self, obj):
        objects = []
        for _object in obj.projectnearerobjects_set.all():
            objects.append(
                {
                    "id": _object.id,
                    "location": _object.location,
                    "type": _object.type,
                    "title": _object.title,
                    "infoLeft": _object.infoLeft,
                    "infoRight": _object.infoRight,
                }
            )
        return objects

    def get_projectBenefits(self, obj):
        benefits = []
        for benefit in obj.projectbenefit_set.all():
            benefits.append(
                {
                    "title": benefit.title,
                    "icon": benefit.icon.name,
                    "image": benefit.image.name,
                    "text": benefit.text,
                    "additionalText": benefit.additionalText,
                    "video": benefit.video,
                    "photos": [
                        photo.photo.name
                        for photo in benefit.projectbenefitimage_set.all()
                    ],
                }
            )
        return benefits

    def get_constructionReports(self, obj):
        reports = []
        for report in obj.projectconstructionreport_set.all():
            reports.append(
                {
                    "date": report.date,
                    "photos": [
                        photo.image.name
                        for photo in report.projectconstructionreportimage_set.all()
                    ],
                }
            )
        return reports
