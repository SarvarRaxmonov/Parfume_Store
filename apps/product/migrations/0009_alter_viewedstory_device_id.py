# Generated by Django 4.2.5 on 2023-09-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0008_alter_storycontent_photo_alter_storycontent_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="viewedstory",
            name="device_id",
            field=models.CharField(max_length=900),
        ),
    ]
