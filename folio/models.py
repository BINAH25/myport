from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    message = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)