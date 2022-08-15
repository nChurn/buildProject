from django.db import models

from utils.models import MixinDateModel


class BackCall(MixinDateModel):
    STATUSES = (
        (
            "new",
            "New",
        ),
        (
            "completed",
            "Completed",
        ),
    )
    pageName = models.CharField(max_length=128, blank=True, null=True)
    pageUrl = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    form = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=9, choices=STATUSES, blank=True, null=True)
    adminComment = models.CharField(max_length=1000, blank=True, null=True)
