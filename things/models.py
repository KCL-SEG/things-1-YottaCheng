from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator

class Thing(models.Model):
   name = models.CharField(max_length=30, unique=True)
   description = models.TextField()
   quantity = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

   def __str__(self):
     return self.name