from django.core.exceptions import ValidationError
from django.db import models

from apps.common.models import BaseModel
from apps.product.choices import CurrencyChoices, VolumeChoices


class ProductImage(models.Model):
    file = models.FileField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.file.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField()

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_main = models.BooleanField()

    def __str__(self):
        return self.name


class ProductBrand(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField()

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Volume(models.Model):
    images = models.ManyToManyField(ProductImage)
    size = models.IntegerField(default=0)
    type = models.CharField(max_length=10, choices=VolumeChoices.choices)
    is_available = models.BooleanField()

    def __str__(self):
        return f"{self.size} {self.type}"


class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()
    currency = models.CharField(max_length=10, choices=CurrencyChoices.choices)
    is_recommended = models.BooleanField()
    is_available = models.BooleanField()
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    description = models.TextField()
    discount = models.IntegerField()
    expire_time = models.DateTimeField()
    images = models.ManyToManyField(ProductImage)
    section = models.ManyToManyField(Section)
    tags = models.ManyToManyField(ProductTag)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=True)
    volume = models.ManyToManyField(Volume, blank=True)

    def __str__(self):
        return self.name


class Banner(BaseModel):
    image = models.FileField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    is_main = models.BooleanField()

    def __str__(self):
        return f"Banner for {self.product or self.section}"

    def save(self, *args, **kwargs):
        if self.product and self.section:
            raise ValidationError("Choose either product or section, not both.")
        elif not self.section and not self.product:
            raise ValidationError("Choose either product or section.")
        else:
            super().save(*args, **kwargs)


class StoryContent(BaseModel):
    name = models.CharField(max_length=255)
    video = models.FileField(blank=True, null=True)
    photo = models.FileField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.video and self.photo:
            raise ValidationError("Choose either photo or video, not both.")
        elif not self.video and not self.photo:
            raise ValidationError("Choose either video or photo.")
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Story(BaseModel):
    name = models.CharField(max_length=255)
    content = models.ManyToManyField(StoryContent)
    is_main = models.BooleanField()

    def __str__(self):
        return self.name


class ViewedStory(BaseModel):
    story = models.ForeignKey(StoryContent, on_delete=models.CASCADE, blank=True, null=True)
    device_id = models.CharField(max_length=900)

    def __str__(self):
        return self.story.name
