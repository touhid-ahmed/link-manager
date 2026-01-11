from django.db import models
from django.utils import timezone

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=100)
    link_url = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
