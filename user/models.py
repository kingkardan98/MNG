from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField()
    email = models.EmailField()
    password = models.TextField()

    moneyAvailability = models.FloatField()
    spendingLimit = models.FloatField()