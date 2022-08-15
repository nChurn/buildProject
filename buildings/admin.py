from django.contrib import admin

from buildings import models

# Register your models here.


@admin.register(models.Building)
class BuildingAdmin(admin.ModelAdmin):
    inlines = []
