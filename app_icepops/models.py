from django.db import models

# Create your models here.
class Icepop(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    special_price = models.IntegerField(null=True)
    is_premium = models.BooleanField(default=False)
    promo_end_at = models.DateTimeField(null=True)
    description = models.TextField(null=True)
