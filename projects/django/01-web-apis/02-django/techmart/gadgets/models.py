"""Model File containing the definitions for Brands and Gadgets"""

from django.db import models

class Brand(models.Model):
    """Defines the Brand or the Manufacturer of Gadgets"""
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    description = models.TextField(max_length=800, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"""{self.name}"""


class Gadget(models.Model):
    """Defines the Product or the Gadget and it's details"""
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="gadgets")
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=800, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self) -> str:
        return f"""{self.name}"""
