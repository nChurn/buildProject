from rest_framework import serializers

from pages import models


class PageDetailSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source="content")

    class Meta:
        model = models.Page
        fields = ["title", "titleImage", "slug", "body", "description"]


class PageListSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source="content")

    class Meta:
        model = models.Page
        fields = ["title", "titleImage", "description", "slug"]
