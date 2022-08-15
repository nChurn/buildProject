# Generated by Django 4.1 on 2022-08-15 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bank",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32)),
                ("logo", models.ImageField(upload_to="bank")),
                ("info", models.TextField()),
                ("minSum", models.PositiveIntegerField()),
                ("maxSum", models.PositiveIntegerField()),
                ("minTerm", models.PositiveIntegerField()),
                ("maxTerm", models.PositiveIntegerField()),
                ("minRate", models.CharField(max_length=6)),
                ("withMatCapital", models.BooleanField()),
                ("withFamilyMortgage", models.BooleanField()),
                ("withArmyMortgage", models.BooleanField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=64)),
                ("favicon", models.ImageField(upload_to="organization/favicon")),
                ("logoHeader", models.ImageField(upload_to="organization/header")),
                ("logoFooter", models.ImageField(upload_to="organization/footer")),
                ("privacyPolicy", models.TextField(blank=True, null=True)),
                ("termsConditions", models.TextField(blank=True, null=True)),
                ("copyright", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrganizationSocials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=32)),
                ("url", models.CharField(max_length=256)),
                (
                    "icon",
                    models.FileField(
                        blank=True, null=True, upload_to="organization/social/icon"
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrganizationSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("workDays", models.CharField(max_length=6)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrganizationEmail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254)),
                ("isMain", models.BooleanField(blank=True, null=True)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrganizationAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=256)),
                ("isMain", models.BooleanField(blank=True, null=True)),
                ("isVisible", models.BooleanField(blank=True, null=True)),
                ("tel", models.CharField(blank=True, max_length=11, null=True)),
                ("fax", models.CharField(blank=True, max_length=11, null=True)),
                ("address", models.CharField(blank=True, max_length=256, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("location", models.CharField(blank=True, max_length=32, null=True)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]