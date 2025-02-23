from django.db import models

class Airport(models.Model):
    code= models.CharField(max_length=5)
    city= models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


# Create your models here.
class Flight(models.Model):
    origin =models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"
    
class Passengers(models.Model):
   first=models.CharField(max_length=64)
   last=models.CharField(max_length=64)
   flight=models.ManyToManyField(Flight , related_name="passengers")

   def __str__(self):
       return f"{self.first} {self.last}"