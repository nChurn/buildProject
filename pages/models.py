from django.db import models

from utils.models import MixinDateModel

# Create your models here.


class Page(MixinDateModel):
    titleImage = models.ImageField(upload_to="page")
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(blank=True, null=True)
    isVisible = models.BooleanField(blank=True, null=True)
    availableUntill = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
