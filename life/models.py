from django.db import models

class Aircraft(models.Model):
    identifier = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Flight(models.Model):
    date = models.DateField(auto_now_add=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    route = models.CharField(max_length=50)
    duration = models.DecimalField(max_digits=6, decimal_places=3)
    landings = models.IntegerField()