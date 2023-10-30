from django.db import models

# Create your models here.
class React(models.Model):
  symbol = models.CharField(max_length=30)
  name = models.CharField(max_length=200)
  actual_price = models.FloatField(max_length=5)
  date = models.DateField()

