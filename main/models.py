from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    connection = models.TextField(default='')
    attack = models.IntegerField(default='0000000', editable=False)
    defense = models.IntegerField(default='0000000', editable=False)
    date_added = models.DateField(auto_now_add=True)