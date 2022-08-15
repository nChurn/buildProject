from django.db import models

from utils.models import MixinDateModel
from projects.models import Project

# Create your models here.
class Publication(MixinDateModel):
    TYPES = (
        ("news", "News",),
        ("promo", "Promo",),
    )

    category = models.CharField(choices=TYPES, max_length=5)
    image = models.ImageField(upload_to="publications", blank=True, null=True)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    isVisible = models.BooleanField(blank=True, null=True)
    availableUntill = models.DateTimeField(blank=True, null=True)
    projects = models.ManyToManyField(Project)


class PublicationGallery(MixinDateModel):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="publications/gallery")
    desc = models.TextField()
