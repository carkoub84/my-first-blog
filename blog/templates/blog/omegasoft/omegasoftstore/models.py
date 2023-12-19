# File: Omegasoft/models.py
# Purpose: Define models for the Omegasoft app

from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()