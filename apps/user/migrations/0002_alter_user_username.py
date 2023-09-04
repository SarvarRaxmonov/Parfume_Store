# Generated by Django 4.2.4 on 2023-09-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True,
                unique=True,
                verbose_name="username",
            ),
        ),
    ]
