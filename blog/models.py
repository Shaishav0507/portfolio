from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return self.title