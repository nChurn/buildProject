from django.contrib import admin

from floors import models

# Register your models here.


@admin.register(models.FloorLayout)
class FloorLayoutAdmin(admin.ModelAdmin):
    inlines = []


@admin.register(models.Floor)
class FloorLayoutAdmin(admin.ModelAdmin):
    inlines = []
