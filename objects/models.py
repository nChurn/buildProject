from django.db import models

from utils.models import MixinDateModel
from layouts.models import Layout
from buildings.models import Building
from projects.models import Project
from floors.models import Floor
from sections.models import Section

# Create your models here.
class Object(MixinDateModel):
    STATUSES = (
        ("hidden", "Hidden",),
        ("available", "Available",),
        ("booked", "Booked",),
        ("sold", "Sold",),
    )
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE, blank=True, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True
    )
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, max_length=9)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    entrance = models.ForeignKey(
        Section, on_delete=models.CASCADE, blank=True, null=True
    )
    price = models.PositiveIntegerField(blank=True, null=True)
    meterPrice = models.PositiveIntegerField(blank=True, null=True)
    finishing = models.CharField(max_length=32, blank=True, null=True)
    openDate = models.DateField(blank=True, null=True)


# Раздел объекты поблизости
class ProjectNearerObjects(MixinDateModel):
    TYPES = (
        ("culture", "Culture",),
        ("medicine", "Medicine",),
        ("education", "Education",),
        ("shop", "Shop",),
        ("food", "Food",),
        ("sport", "Sport",),
        ("transport", "Transport",),
        ("kindergarten", "Kindergarten",),
    )
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    location = models.CharField(max_length=32)
    type = models.CharField(choices=TYPES, max_length=12)
    title = models.CharField(max_length=32)
    infoLeft = models.CharField(max_length=256)
    infoRight = models.CharField(max_length=256)
