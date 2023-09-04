# Generated by Django 4.2.5 on 2023-09-04 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_productimage_file_alter_productimage_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="type",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.producttype",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="volume",
            field=models.ManyToManyField(blank=True, to="product.volume"),
        ),
    ]
