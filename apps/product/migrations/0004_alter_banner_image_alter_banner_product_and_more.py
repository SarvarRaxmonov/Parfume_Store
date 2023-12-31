# Generated by Django 4.2.5 on 2023-09-04 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_product_type_alter_product_volume"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banner",
            name="image",
            field=models.FileField(blank=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="banner",
            name="product",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.product",
            ),
        ),
        migrations.AlterField(
            model_name="banner",
            name="section",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.section",
            ),
        ),
    ]
