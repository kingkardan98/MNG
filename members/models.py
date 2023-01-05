from django.db import models
from django.urls import reverse

from simple_history.models import HistoricalRecords

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)

    availability = models.DecimalField(max_digits=10000, decimal_places=2)
    spendable = models.DecimalField(max_digits=10000, decimal_places=2, db_column='spending')

    author = models.CharField(max_length=256, default='')

    history = HistoricalRecords()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def unpack(self):
        return {
                'name': self.name, 
                'email': self.email, 
                'availability': self.availability, 
                'spendable': self.spendable, 
                'author': self.author
                }
