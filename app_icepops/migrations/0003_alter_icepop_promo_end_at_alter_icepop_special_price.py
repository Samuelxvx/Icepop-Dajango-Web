# Generated by Django 4.1.5 on 2023-01-13 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_icepops", "0002_icepop_description_icepop_special_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="icepop",
            name="promo_end_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="icepop",
            name="special_price",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
