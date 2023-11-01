from django.db import models

# Create your models here.
class React(models.Model):
  symbol = models.CharField(unique=True,max_length=30, primary_key=True)
  name = models.CharField(max_length=200)
  actual_price = models.FloatField(max_length=5)
  date = models.DateTimeField(max_length=200, primary_key=False)
  monitor = models.IntegerField()
  low = models.FloatField(max_length=5)
  high = models.FloatField(max_length=5)
  min = models.FloatField(max_length=5)
  max = models.FloatField(max_length=5)



