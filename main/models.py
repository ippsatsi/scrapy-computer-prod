from django.db import models

# Create your models here.

from django.utils import timezone

class Quote(models.Model):
    """
    The scrapped data will be saved in this model
    """
    text = models.TextField()
    author = models.CharField(max_length=512)
    fecha = models.DateField(default=timezone.now)