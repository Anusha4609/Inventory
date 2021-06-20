from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=256)
    googleid = models.CharField(max_length=256)
    quantity = models.IntegerField()
