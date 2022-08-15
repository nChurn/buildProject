from rest_framework import serializers
from . import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrganizationAddress
        fields = [
            "name",
            "isMain",
            "isVisible",
            "tel",
            "fax",
            "address",
            "email",
            "location",
        ]


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["workDays", "workTime"]
        model = models.OrganizationSchedule


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["email", "isMain"]


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["title", "url", "icon"]
        model = models.OrganizationSocials


class OrganizationSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    schedule = ScheduleSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    socials = SocialSerializer(many=True, read_only=True)

    class Meta:
        model = models.Organization
        fields = [
            "name",
            "favicon",
            "logoHeader",
            "logoFooter",
            "privacyPolicy",
            "termsConditions",
            "copyright",
            "addresses",
            "schedule",
            "emails",
            "socials",
        ]


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = [
            "id",
            "name",
            "logo",
            "info",
            "minSum",
            "maxSum",
            "maxTerm",
            "minRate",
            "withMatCapital",
            "withFamilyMortgage",
            "withArmyMortgage",
        ]
