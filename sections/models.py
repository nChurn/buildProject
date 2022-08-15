from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MinLengthValidator,
)

from utils.models import MixinDateModel
from buildings.models import Building

# Create your models here.
class Section(MixinDateModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, validators=[MinLengthValidator(2)])
    masterPlanImage = models.ImageField(
        upload_to="section/master",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )
    polygonData = models.JSONField(blank=True, null=True)
