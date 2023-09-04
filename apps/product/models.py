from django.db import models

from apps.common.models import BaseModel
from apps.product.choices import CurrencyChoices, VolumeChoices


class ProductImage(models.Model):
    file = models.FileField()
    url = models.URLField()

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
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    volume = models.ManyToManyField(Volume)

    def __str__(self):
        return self.name


class Banner(BaseModel):
    image = models.FileField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    is_main = models.BooleanField()

    def __str__(self):
        return f"Banner for {self.product.name or self.section.name}"


class StoryContent(BaseModel):
    name = models.CharField(max_length=255)
    video = models.FileField()
    photo = models.FileField()

    def __str__(self):
        return self.name


class Story(BaseModel):
    name = models.CharField(max_length=255)
    content = models.ManyToManyField(StoryContent)

    def __str__(self):
        return self.name
