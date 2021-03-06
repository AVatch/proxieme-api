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


BIDS         = ( ('00', 'FREE'),
                 ('01', '0.99'),
                 ('02', '4.99'),
                 ('03', '9.99'),
                 ('04', '49.99'),
                 ('05', '99.99'),
               )

class Bid(models.Model):
    bid = models.CharField(max_length=2, choices=BIDS)
    bidder = models.ForeignKey(Account)
    proxie = models.ForeignKey(Proxie)

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time_created',)


class ProxieSession(models.Model):
    sessionID = models.CharField(max_length=500)
    surrogateID = models.CharField(max_length=500)
    requesterID = models.CharField(max_length=500)

    bid = models.ForeignKey(Bid, related_name='PSbid')
    proxie = models.ForeignKey(Proxie, related_name='PSproxie')
    surrogate = models.ForeignKey(Account, related_name='PSsurrogate')
    requester = models.ForeignKey(Account, related_name='PSrequester')

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time_created',)

