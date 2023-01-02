from django.db import models
from django.urls import reverse

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)

    availability = models.DecimalField(max_digits=10000, decimal_places=2)
    spendable = models.DecimalField(max_digits=10000, decimal_places=2, db_column='spending')

    author = models.CharField(max_length=256, default='')