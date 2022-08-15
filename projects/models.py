from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator

from utils.models import MixinDateModel

# Create your models here.


class City(MixinDateModel):
    name = models.CharField(max_length=256)
    active = models.BooleanField(blank=True, null=True)


class Project(MixinDateModel):
    STATUSES = (
        ("active", "Active",),
        ("completed", "Completed",),
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, validators=[MinLengthValidator(2)])
    status = models.CharField(choices=STATUSES, max_length=9)
    description = models.TextField(blank=True, null=True)
    mainImage = models.ImageField(
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )
    masterPlanImage = models.ImageField(
        upload_to="project/master",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )
    address = models.CharField(max_length=256, blank=True, null=True)
    district = models.CharField(max_length=256)
    # позже будет отдельный тип данных
    location = models.CharField(max_length=32, blank=True, null=True)
    discount = models.CharField(max_length=3, blank=True, null=True)
    hasNewBuildings = models.BooleanField(blank=True, null=True)


class ProjectImage(MixinDateModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="project/image",
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )


class ProjectBenefit(MixinDateModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    icon = models.ImageField(
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )
    image = models.ImageField(
        upload_to="project/benefit",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )
    text = models.TextField(blank=True, null=True)
    additionalText = models.TextField(blank=True, null=True)

    video = models.CharField(max_length=512, blank=True, null=True)


class ProjectBenefitImage(MixinDateModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    projectBenefit = models.ForeignKey(ProjectBenefit, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="project/benefit/",
        validators=[FileExtensionValidator(["jpg", "png", "svg"])],
    )


class ProjectConstructionReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField()
    video = models.CharField(max_length=512, blank=True, null=True)
    stream = models.CharField(max_length=512, blank=True, null=True)


class ProjectConstructionReportImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    constructionReports = models.ForeignKey(
        ProjectConstructionReport, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project/cunstruction_report")
