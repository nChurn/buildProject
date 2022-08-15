from django.db import models
from utils.models import MixinDateModel

# Create your models here.


class Company(MixinDateModel):
    title = models.CharField(max_length=32)
    titleImage = models.ImageField(upload_to="company")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    mainText = models.TextField(blank=True, null=True)
    mapImage = models.ImageField(upload_to="company/mainImage", blank=True, null=True)


class CompanyAchievements(MixinDateModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="company/achievements")
    title = models.CharField(max_length=32)
    text = models.CharField(max_length=256)


class CompanyAwards(MixinDateModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="company/awards")
    title = models.CharField(max_length=32)
    text = models.CharField(max_length=256)


class CompanyHistory(MixinDateModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to="company/history")
    title = models.CharField(max_length=64)
    desc = models.TextField()


class CompanyAboutBlock(MixinDateModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    shortTitle = models.CharField(max_length=64)
    shortText = models.TextField()
    image = models.ImageField(upload_to="company/about")


class Investor(MixinDateModel):
    title = models.CharField(max_length=64)
    titleImage = models.ImageField(upload_to="investors")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)


class InvestorFinancialInfo(MixinDateModel):
    INDICATOR_TYPES = (
        ("financial", "Financial",),
        ("operating", "Operating",),
    )
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    indicatorType = models.CharField(choices=INDICATOR_TYPES, max_length=9)
    age = models.PositiveIntegerField()
    revenue = models.CharField(max_length=5, blank=True, null=True)
    editda = models.CharField(max_length=5, blank=True, null=True)
    editdaMargin = models.CharField(max_length=5, blank=True, null=True)
    netProfit = models.CharField(max_length=5, blank=True, null=True)
    netProfitMargin = models.CharField(max_length=5, blank=True, null=True)
    assets = models.CharField(max_length=5, blank=True, null=True)
    debt = models.CharField(max_length=5, blank=True, null=True)
    debtWithNote = models.CharField(max_length=5, blank=True, null=True)
    debtWithNoteByEditda = models.CharField(max_length=5, blank=True, null=True)
    note = models.CharField(max_length=64, blank=True, null=True)


class InvestorOperatingInfo(MixinDateModel):
    INDICATOR_TYPES = (
        ("financial", "Financial"),
        ("operating", "Operating",),
    )
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    indicatorType = models.CharField(choices=INDICATOR_TYPES, max_length=9)
    year = models.PositiveIntegerField()
    residentalRevenue = models.CharField(max_length=5)
    commercialRevenue = models.CharField(max_length=5)
    residentalProceeds = models.CharField(max_length=5)
    salesVolume = models.CharField(max_length=5)
    comissioningVolume = models.CharField(max_length=5)
    mortgageShareOfVolume = models.CharField(max_length=4)


class InvestorDisclosureDocs(MixinDateModel):
    DOCUMENT_CATEGORIES = (
        ("issue", "Issue",),
        ("report", "Report",),
        ("event", "Event",),
        ("docs", "Docs",),
    )
    QUARTERS = (
        (1, 1,),
        (2, 2,),
        (3, 3,),
        (4, 4,),
    )
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    quarter = models.PositiveSmallIntegerField(choices=QUARTERS)
    year = models.PositiveIntegerField()
    file = models.FileField(upload_to="investors/disclosure_docs/")
    fileType = models.CharField(max_length=8)
