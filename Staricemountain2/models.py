from django.db import models

class Temperatures(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=200)
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    total = models.IntegerField()