from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=256, validators=[MinLengthValidator(8)])
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=512, validators=[MinLengthValidator(8)])

    availability = models.DecimalField(max_digits=10000, decimal_places=2)
    spendable = models.DecimalField(max_digits=10000, decimal_places=2, db_column='spending')

    def get_absolute_url(self):
        return f"/user/{self.id}"