# Generated by Django 4.2.5 on 2023-09-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0027_alter_storycontent_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="storycontent",
            name="url_uz",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="storycontent",
            name="url",
            field=models.URLField(blank=True),
        ),
    ]