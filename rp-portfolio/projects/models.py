from django.db import models

# Create your models here.

class Project(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    technologie = models.CharField(max_length=20, blank=True)
    image = models.FilePathField(path="projects/static/projects/img")
