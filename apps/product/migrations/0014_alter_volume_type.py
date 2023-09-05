# Generated by Django 4.2.4 on 2023-09-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0013_volume_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volume",
            name="type",
            field=models.CharField(
                choices=[("kg", "kg"), ("litr", "litr"), ("gr", "gr"), ("ml", "ml")],
                max_length=255,
            ),
        ),
    ]
