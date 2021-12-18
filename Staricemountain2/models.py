from django.db import models

class Staricemountain(models.Model):
    createadd = models.DateTimeField()
    updateadd = models.DateTimeField()
    city = models.CharField(max_length=200)
    maxtemperature = models.FloatField()
    mintemperature = models.FloatField()
    sum = models.IntegerField()