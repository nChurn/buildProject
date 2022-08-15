from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

# Register your models here.
from pages import models


class PageForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Page
        fields = "__all__"


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    form = PageForm
    inlines = []
