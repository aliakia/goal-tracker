from django.db import models

# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    mood = models.CharField(max_length=200)
    entry = models.TextField()

    def __str__(self):
        return self.title