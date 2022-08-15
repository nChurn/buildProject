from django.contrib import admin

from objects import models


@admin.register(models.Object)
class ObjectAdmin(admin.ModelAdmin):
    inlines = []
