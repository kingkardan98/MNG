from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=512)

    moneyAvailability = models.DecimalField(max_digits=10000, decimal_places=2)
    spendingLimit = models.DecimalField(max_digits=10000, decimal_places=2)