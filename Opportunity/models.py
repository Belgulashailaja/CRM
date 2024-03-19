from django.db import models
from Accounts.models import Account

# Create your models here.
class Opportunity(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=50)
    
    def __str__(self):
        return self.account