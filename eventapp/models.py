from django.db import models

# Create your models here.
class Event(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name = models.CharField(max_length=55)
    cus_ph = models.CharField(max_length=12)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"Booking for {self.event.name} by {self.cus_name}"
