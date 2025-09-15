from django.db import models
# from rest_framework import serializers
# Create your models here.

class Employer(models.Model):
    FIO = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'FIO')
    position = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'Position')
    salary = models.FloatField(verbose_name = 'Salary')
    start_date = models.DateField(auto_now = True, verbose_name = 'Start date')

    def __str__(self) -> str:
        return f'{self.pk}) {self.FIO}'