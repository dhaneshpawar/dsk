from django.db import models

# Create your models here.
class Logs(models.Model):
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    username  = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    weburl = models.CharField(max_length=100)

def __str__(self):
    return self.date