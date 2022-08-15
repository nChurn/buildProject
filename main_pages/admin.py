from django.contrib import admin

from main_pages import models

# Register your models here.


class CompanyAchievementsAdmin(admin.StackedInline):
    model = models.CompanyAchievements


class CompanyAwardsAdmin(admin.StackedInline):
    model = models.CompanyAwards


class CompanyHistoryAdmin(admin.StackedInline):
    model = models.CompanyHistory


class CompanyAboutBlockAdmin(admin.StackedInline):
    model = models.CompanyAboutBlock


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        CompanyAchievementsAdmin,
        CompanyAwardsAdmin,
        CompanyHistoryAdmin,
        CompanyAboutBlockAdmin,
    ]


class InvestorFinancialInfoAdmin(admin.StackedInline):
    model = models.InvestorFinancialInfo


class InvestorOperatingInfoAdmin(admin.StackedInline):
    model = models.InvestorOperatingInfo


class InvestorDisclosureDocsAdmin(admin.StackedInline):
    model = models.InvestorDisclosureDocs


@admin.register(models.Investor)
class InvestorAdmin(admin.ModelAdmin):
    inlines = [
        InvestorFinancialInfoAdmin,
        InvestorOperatingInfoAdmin,
        InvestorDisclosureDocsAdmin,
    ]
