from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    omen = models.IntegerField(default=0)
    space = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)