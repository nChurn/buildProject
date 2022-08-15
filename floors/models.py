from django.db import models
from django.core.validators import (    
    MinLengthValidator,
)

from utils.models import MixinDateModel
from buildings.models import Building
from projects.models import Project
from sections.models import Section

# Create your models here.


class FloorLayout(MixinDateModel):
    building = models.ForeignKey(Building, on_delete=models.PROTECT)
    name = models.CharField(max_length=256, validators=[MinLengthValidator(2)])
    schema = models.FileField(upload_to="floor_plan/schema")


class Floor(MixinDateModel):
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE)
    sectionId = models.ForeignKey(Section, on_delete=models.CASCADE)
    # PROBABLY
    floorLayout = models.ForeignKey(FloorLayout, on_delete=models.CASCADE)
    # !!!
    number = models.IntegerField()
    schemeImage = models.ImageField(upload_to="floor/schema", blank=True, null=True)
    polygonData = models.JSONField(blank=True, null=True)
