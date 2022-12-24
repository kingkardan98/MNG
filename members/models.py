from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=256, validators=[MinLengthValidator(8)])
    email = models.EmailField(max_length=256)

    availability = models.DecimalField(max_digits=10000, decimal_places=2)
    spendable = models.DecimalField(max_digits=10000, decimal_places=2, db_column='spending')

    author = models.CharField(max_length=256, default='')

    def get_absolute_url(self):
        return reverse("user_detail_view", kwargs={"id": self.id})