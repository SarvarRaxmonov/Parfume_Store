# Generated by Django 4.2.5 on 2023-09-06 06:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0003_order_review_liked"),
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
        migrations.AlterModelOptions(
            name="userphone",
            options={
                "verbose_name": "User Phone",
                "verbose_name_plural": "User Phones",
            },
        ),
        migrations.AddField(
            model_name="accreditation",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="accreditation",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="bankcard",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="bankcard",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="district",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="district",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="liked",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="liked",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="is_delivered",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="region",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="region",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AddField(
            model_name="userphone",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="userphone",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
        migrations.AlterField(
            model_name="accreditation",
            name="district",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="district",
                to="cart.district",
                verbose_name="District",
            ),
        ),
        migrations.AlterField(
            model_name="accreditation",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="region",
                to="cart.region",
                verbose_name="Region",
            ),
        ),
        migrations.AlterField(
            model_name="accreditation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="bankcard",
            name="accreditation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="cart.accreditation",
                verbose_name="Accreditation",
            ),
        ),
        migrations.AlterField(
            model_name="bankcard",
            name="number",
            field=models.IntegerField(verbose_name="Number"),
        ),
        migrations.AlterField(
            model_name="bankcard",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="cart",
            name="count",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Count",
            ),
        ),
        migrations.AlterField(
            model_name="cart",
            name="image",
            field=models.ImageField(upload_to="cart_images/", verbose_name="Image"),
        ),
        migrations.AlterField(
            model_name="cart",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Price"
            ),
        ),
        migrations.AlterField(
            model_name="cart",
            name="title",
            field=models.CharField(max_length=125, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="district",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="district_region",
                to="cart.region",
                verbose_name="Region",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="type",
            field=models.CharField(
                choices=[
                    ("accepted", "Accepted"),
                    ("delivered", "Delivered"),
                    ("during_delivery", "During Delivery"),
                    ("canceled", "Canceled"),
                ],
                default="during_delivery",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="accreditation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="cart.accreditation",
                verbose_name="Accreditation",
            ),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="name",
            field=models.CharField(max_length=125, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Phone Number",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="userphone",
            name="accreditation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="cart.accreditation",
                verbose_name="Accreditation",
            ),
        ),
        migrations.AlterField(
            model_name="userphone",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, verbose_name="Phone Number"
            ),
        ),
        migrations.AlterField(
            model_name="userphone",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]