from rest_framework import serializers

from forms import models


class BackCallCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BackCall
        fields = ["pageName", "pageUrl", "phone", "name", "form"]
