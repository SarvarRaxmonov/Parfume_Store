# Generated by Django 4.2.4 on 2023-09-05 11:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0004_accreditation_created_at_accreditation_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="liked",
            options={"verbose_name": "Liked", "verbose_name_plural": "Liked"},
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Order", "verbose_name_plural": "Orders"},
        ),
        migrations.AlterModelOptions(
            name="review",
            options={"verbose_name": "Review", "verbose_name_plural": "Reviews"},
        ),
    ]
