from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from news import models

# Register your models here.


class PublicationGalleryAdmin(admin.StackedInline):
    model = models.PublicationGallery


class PublicationForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Publication
        fields = "__all__"


@admin.register(models.Publication)
class PublicationAdmin(admin.ModelAdmin):
    form = PublicationForm
    inlines = [PublicationGalleryAdmin]
