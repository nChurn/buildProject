from django.db import models
from django.core.validators import (
    FileExtensionValidator,
)

from utils.models import MixinDateModel

from projects.models import Project
from buildings.models import Building
from sections.models import Section
from floors.models import FloorLayout, Floor


class Layout(MixinDateModel):
    CATEGORIES = (
        ("flat","Flat",),
        ("larder","Larder",),
        ("parking", "Parking",),
        ("office", "Office",),
    )
    LAYOUTS = (
        ("studio","Studio",),
        ("one_room", "One_room",),
        ("two_room", "Two_room",),
        ("three_room", "Three_room",),
        ("four_room", "Four_room",),
    )
    WINDOWS_POSITION = (
        ("north", "North",),
        ("northeast","Northeast",),
        ("east","East",),
        ("southeast", "Southeast",),
        ("south", "South",),
        ("southwest", "Southwest",),
        ("west", "West",),
        ("northwest", "Northwest",),
    )

    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE)
    sectionId = models.ForeignKey(Section, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=32)
    category = models.CharField(choices=CATEGORIES, max_length=7)
    # внешний id
    layoutType = models.CharField(max_length=10, choices=LAYOUTS, blank=True, null=True)
    floorLayout = models.ForeignKey(FloorLayout, on_delete=models.CASCADE)
    polygonData = models.JSONField(blank=True, null=True)
    space = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    livingSpace = models.DecimalField(
        max_digits=6, decimal_places=1, blank=True, null=True
    )
    spaceWithBalcony = models.DecimalField(
        max_digits=6, decimal_places=1, blank=True, null=True
    )
    balconyCount = models.PositiveSmallIntegerField(blank=True, null=True)
    windowsPosition = models.CharField(
        choices=WINDOWS_POSITION, max_length=9, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)


class LayoutDescriptionImage(MixinDateModel):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="layout/description/image",
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )


class LayoutImage(MixinDateModel):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="layout/image",
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )
