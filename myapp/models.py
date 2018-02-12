from django.db import models


class Item(models.Model):
    item_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class price(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    price_text = models.CharField(max_length=200)
    actualprice = models.IntegerField(default=0)
# Create your models here.
