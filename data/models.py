from django.db import models

from django.db import models
from django.core.validators import (
    FileExtensionValidator,
)

from utils.models import MixinDateModel

# Create your models here.


class Organization(MixinDateModel):
    name = models.CharField(max_length=64)
    favicon = models.ImageField(upload_to="organization/favicon")
    logoHeader = models.ImageField(upload_to="organization/header")
    logoFooter = models.ImageField(upload_to="organization/footer")
    privacyPolicy = models.TextField(blank=True, null=True)
    termsConditions = models.TextField(blank=True, null=True)
    copyright = models.TextField(blank=True, null=True)


class OrganizationAddress(MixinDateModel):
    name = models.CharField(max_length=256)
    isMain = models.BooleanField(blank=True, null=True)
    isVisible = models.BooleanField(blank=True, null=True)
    tel = models.CharField(max_length=11, blank=True, null=True)
    fax = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    # дальше будет отдельный тип данных
    location = models.CharField(max_length=32, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class OrganizationSchedule(MixinDateModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    workDays = models.CharField(max_length=6)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class OrganizationEmail(MixinDateModel):
    email = models.EmailField()
    isMain = models.BooleanField(blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class OrganizationSocials(MixinDateModel):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    icon = models.FileField(upload_to="organization/social/icon", blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Bank(MixinDateModel):
    name = models.CharField(max_length=32)
    logo = models.ImageField(
        upload_to="bank", validators=[FileExtensionValidator(["jpg", "png", "svg"])]
    )
    info = models.TextField()
    minSum = models.PositiveIntegerField()
    maxSum = models.PositiveIntegerField()
    minTerm = models.PositiveIntegerField()
    maxTerm = models.PositiveIntegerField()
    minRate = models.CharField(max_length=6)
    withMatCapital = models.BooleanField()
    withFamilyMortgage = models.BooleanField()
    withArmyMortgage = models.BooleanField()
