from django.contrib import admin

from layouts import models

# Register your models here.


class LayoutDescriptionImageAdmin(admin.StackedInline):
    model = models.LayoutDescriptionImage


class LayoutImageAdmin(admin.StackedInline):
    model = models.LayoutImage


@admin.register(models.Layout)
class LayoutAdmin(admin.ModelAdmin):
    inlines = [
        LayoutDescriptionImageAdmin,
        LayoutImageAdmin,
    ]
