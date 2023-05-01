from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=30, unique=True)
    item_price = models.IntegerField(null=False, default=0)
    item_img = models.ImageField(null=False )
    item_filter = models.CharField(max_length=30, default="unisex")
    item_stocks = models.IntegerField(null=False, default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS  = ['item_name', 'item_price', 'item_img', 'item_stocks', 'date_added', ]

    def __str__(self):
        return self.item_name

class CartItem(models.Model):
    c_item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)

    
        

    