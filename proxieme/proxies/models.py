from django.db import models
from accounts.models import Account


class Proxie(models.Model):
    proxie = models.CharField(max_length=140)
    description = models.TextField(blank=True)

    account = models.ForeignKey(Account)
    
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time_created',)