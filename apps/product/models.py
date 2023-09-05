from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
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


class ProductCategoryViewed(BaseModel):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="view_to_category")
    device_id = models.CharField(max_length=900)

    def __str__(self):
        return self.category.name


class Section(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="section_category")
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
    is_available = models.BooleanField()
    type = models.CharField(max_length=255, choices=VolumeChoices.choices)

    def __str__(self):
        return f"{self.size} {self.is_available}"


class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()
    currency = models.CharField(max_length=10, choices=CurrencyChoices.choices)
    is_recommended = models.BooleanField()
    is_available = models.BooleanField()
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    description = models.TextField()
    discount = models.IntegerField(validators=[MaxValueValidator(100)])
    expire_time = models.DateTimeField()
    images = models.ManyToManyField(ProductImage)
    section = models.ForeignKey(
        Section,
        on_delete=models.DO_NOTHING,
        related_name="product_section",
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(ProductTag)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    volume = models.ManyToManyField(Volume, blank=True)

    def __str__(self):
        return self.name


class Banner(BaseModel):
    name = models.CharField(max_length=800, blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(blank=True)
    url = models.URLField()
    is_main = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.is_main}"


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
    content = models.ManyToManyField(StoryContent, related_name="story_to_content")
    is_main = models.BooleanField()

    def __str__(self):
        return self.name


class ViewedStory(BaseModel):
    story = models.ForeignKey(StoryContent, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=900)

    def __str__(self):
        return self.story.name


class SearchKeyword(models.Model):
    keyword = models.CharField(max_length=1000)
    device_id = models.CharField(max_length=900)
