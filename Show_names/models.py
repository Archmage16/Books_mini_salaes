from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, blank=True, null=True)
    homeworld = models.CharField(max_length=100, blank=True, null=True)
    birth_year = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name