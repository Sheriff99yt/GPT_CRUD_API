# filehandler/models.py
from django.db import models

class File(models.Model):
    id = models.BigAutoField(primary_key=True)  # Use BigAutoField for larger IDs
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name
