from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.TimeField()

    def __str__(self):
        return f"{self.first_name} - {self.reservation_date} at {self.reservation_slot}"
