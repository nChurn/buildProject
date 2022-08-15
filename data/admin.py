from django.contrib import admin

from data import models

# Register your models here.


class OrganizationAddressAdmin(admin.StackedInline):
    model = models.OrganizationAddress


class OrganizationScheduleAdmin(admin.StackedInline):
    model = models.OrganizationSchedule


class OrganizationEmailAdmin(admin.StackedInline):
    model = models.OrganizationEmail


class OrganizationSocialsAdmin(admin.StackedInline):
    model = models.OrganizationSocials


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [
        OrganizationAddressAdmin,
        OrganizationScheduleAdmin,
        OrganizationEmailAdmin,
        OrganizationSocialsAdmin,
    ]


@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    inlines = []
