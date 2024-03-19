from django.db import models
from Accounts.models import Account

# Create your models here.
class Document(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.account