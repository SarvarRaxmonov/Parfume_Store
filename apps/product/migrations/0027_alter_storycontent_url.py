# Generated by Django 4.2.5 on 2023-09-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0026_storycontent_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storycontent",
            name="url",
            field=models.URLField(),
        ),
    ]
