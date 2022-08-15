from rest_framework import serializers

from main_pages import models


class CompanyAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyAwards
        fields = ["title", "text", "image"]


class CompanyAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyAchievements
        fields = ["title", "text", "image"]


class CompanyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyHistory
        fields = ["year", "image", "title", "desc"]


class CompanyAboutBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyAboutBlock
        fields = ["title", "text", "shortTitle", "shortText", "image"]


class CompanySerializer(serializers.ModelSerializer):
    awards = CompanyAwardsSerializer(many=True, source="companyawards_set")
    achievements = CompanyAchievementsSerializer(
        many=True, source="companyachievements_set"
    )
    history = CompanyHistorySerializer(
        many=True, read_only=True, source="companyhistory_set"
    )
    aboutBlocks = CompanyAboutBlockSerializer(
        many=True, read_only=True, source="companyaboutblock_set"
    )

    class Meta:
        model = models.Company
        fields = [
            "title",
            "titleImage",
            "slug",
            "description",
            "mainText",
            "mapImage",
            "awards",
            "achievements",
            "history",
            "aboutBlocks",
        ]


class InvestorFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvestorFinancialInfo
        fields = [
            "age",
            "revenue",
            "editda",
            "editdaMargin",
            "netProfit",
            "netProfitMargin",
            "assets",
            "debt",
            "debtWithNote",
            "debtWitjNoteByEditda",
            "note",
        ]


class InvestorOperatingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvestorOperatingInfo
        fields = [
            "year",
            "residentalRevenue",
            "commercialRevenue",
            "residentalProceeds",
            "salesVolume",
            "comissioningVolume",
            "mortgageShareOfVolume",
        ]


class InvestorDisclosureDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvestorDisclosureDocs
        fields = ["id", "title", "fileType", "file", "quarter", "year"]


class InvestorSerializer(serializers.ModelSerializer):
    financialInfo = InvestorFinancialInfoSerializer(
        many=True, source="investorfinancialinfo_set"
    )
    operatingInfo = InvestorOperatingInfoSerializer(
        many=True, source="investoroperatinginfo_set"
    )
    disclosureDocs = InvestorDisclosureDocsSerializer(
        many=True, source="investordisclosuredocs_set"
    )

    class Meta:
        model = models.Investor
        fields = [
            "title",
            "titleImage",
            "slug",
            "description",
            "financialInfo",
            "operatingInfo",
            "disclosureDocs",
        ]
