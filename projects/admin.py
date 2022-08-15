from django.contrib import admin

from projects import models
from objects.models import ProjectNearerObjects

# Register your models here.


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    inlines = []


class ProjectImageAdmin(admin.StackedInline):
    model = models.ProjectImage


class ProjectBenefitAdmin(admin.StackedInline):
    model = models.ProjectBenefit


class ProjectBenefitImageAdmin(admin.StackedInline):
    model = models.ProjectBenefitImage


class ProjectConstructionReportAdmin(admin.StackedInline):
    model = models.ProjectConstructionReport


class ProjectConstructionReportImageAdmin(admin.StackedInline):
    model = models.ProjectConstructionReportImage


class ProjectNearerObjectsAdmin(admin.StackedInline):
    model = ProjectNearerObjects


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectImageAdmin,
        ProjectBenefitAdmin,
        ProjectBenefitImageAdmin,
        ProjectConstructionReportAdmin,
        ProjectConstructionReportImageAdmin,
        ProjectNearerObjectsAdmin,
    ]
