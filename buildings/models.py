from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
    MinLengthValidator,
)

from utils.models import MixinDateModel
from projects.models import Project

# Create your models here.


class Building(MixinDateModel):
    STATUSES = (
        ("hidden", "Hidden",),
        ("construction", "Construction",),
        ("ready", "Ready",),
        ("success", "Success",),
    )
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    name = models.CharField(max_length=256, validators=[MinLengthValidator(2)])
    status = models.CharField(choices=STATUSES, max_length=12)
    masterPlanImage = models.ImageField(
        upload_to="building/master",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )
    image = models.ImageField(
        upload_to="building/image",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )
    openDate = models.DateField()
    readyPercent = models.PositiveIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    polygonData = models.JSONField(blank=True, null=True)
