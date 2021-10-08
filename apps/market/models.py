from django.db import models
from django.utils.html import mark_safe
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Action(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    message = models.TextField()
    image = models.ImageField(upload_to='message/thumbnail', null=True, blank=True)

    def __str__(self):
        return self.message


class Sell(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.FloatField()
    is_certified = models.BooleanField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'Selling : {self.item} for {self.price}'
    