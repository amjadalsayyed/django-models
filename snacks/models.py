from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Snack (models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default='bla bla bla ..')
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)