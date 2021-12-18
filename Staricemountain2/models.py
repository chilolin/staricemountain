from django.db import models

class Temperatures(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.TextField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    total = models.FloatField()