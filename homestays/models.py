from django.db import models

class Homestay(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.IntegerField()

    def __str__(self):
        return self.name
