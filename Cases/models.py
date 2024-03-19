from django.db import models
from Accounts.models import Account
from Contacts.models import Contact

# Create your models here.
class Case(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.account