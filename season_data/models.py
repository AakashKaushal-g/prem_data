from django.db import models

# Create your models here.

FOOT_CHOICES = [('L','Left'),('R','Right'),('N','Not Available')]
class Season(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    country = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.name} ({self.country}) | {self.start_year}-{str(self.end_year).strip(' ')[-2:]}"