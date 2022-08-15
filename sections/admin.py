from django.contrib import admin

from sections import models

# Register your models here.


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = []
