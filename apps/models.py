from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Model, CharField, DecimalField, TextField


class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField(null=True, blank=True)
