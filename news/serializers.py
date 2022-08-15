from rest_framework import serializers

from news import models


class PublicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publication
        fields = ["id", "category", "title", "description", "createdAt"]


class PublicationGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PublicationGallery
        fields = ["image", "title"]


class PublicationListSerializer(serializers.ModelSerializer):
    gallery = PublicationGallerySerializer(many=True, source="publicationgallery_set")
    text = serializers.CharField(source="content")

    class Meta:
        model = models.Publication
        fields = [
            "id",
            "category",
            "title",
            "description",
            "createdAt",
            "text",
            "gallery",
            "slug",
        ]
