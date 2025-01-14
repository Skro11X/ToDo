from django.db import models

class Task(models.Model):

    status = models.BooleanField(default=False)
    label = models.CharField(max_length=100)
    description = models.TextField()
