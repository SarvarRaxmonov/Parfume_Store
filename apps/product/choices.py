from django.db.models import TextChoices


class CurrencyChoices(TextChoices):
    UZS = "uzs", "UZS"
    RUBL = "rubl", "RUBL"
    USD = "usd", "USD"


class VolumeChoices(TextChoices):
    KG = "kg", "kg"
    LITR = "litr", "litr"
    GR = "gr", "gr"
    ML = "ml", "ml"
