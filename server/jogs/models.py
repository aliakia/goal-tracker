from django.db import models
from .choices import DIFFICULTY_CHOICES

# Create your models here.
class Jogs(models.Model):
    place = models.CharField(max_length=200)
    distance = models.FloatField()
    duration = models.IntegerField()
    date = models.DateField(null=False, auto_now_add=True)
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, max_length=1)

    def __str__(self):
        return f'{self.date} | {self.distance}km in {self.duration} mins.'