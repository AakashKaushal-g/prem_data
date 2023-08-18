from django.db import models

# Create your models here.

FOOT_CHOICES = [('L','Left'),('R','Right'),('N','Not Available')]
class PlayerInfo(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=60)
    position = models.CharField(max_length=15)
    foot = models.CharField(max_length=1,choices=FOOT_CHOICES,default='N')
    birth_date = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.country} | {self.position}"