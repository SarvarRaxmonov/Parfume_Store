# Generated by Django 4.2.5 on 2023-09-08 13:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0028_storycontent_url_uz_alter_storycontent_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="storycontent",
            name="url_uz",
        ),
    ]
