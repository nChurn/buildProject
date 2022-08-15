from django.contrib import admin

from forms import models

# Register your models here.


@admin.register(models.BackCall)
class BackCallAdmin(admin.ModelAdmin):
    inlines = []
