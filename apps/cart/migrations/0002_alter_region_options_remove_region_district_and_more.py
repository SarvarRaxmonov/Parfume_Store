# Generated by Django 4.2.4 on 2023-09-05 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="region",
            options={"verbose_name": "Region", "verbose_name_plural": "Regions"},
        ),
        migrations.RemoveField(
            model_name="region",
            name="district",
        ),
        migrations.AddField(
            model_name="accreditation",
            name="district",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="district",
                to="cart.district",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="district",
            name="region",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="cart.region",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="accreditation",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="region",
                to="cart.region",
            ),
        ),
    ]
