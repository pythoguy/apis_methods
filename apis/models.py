from django.db import models

# Create your models here.


class database(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()