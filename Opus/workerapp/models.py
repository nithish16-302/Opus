from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WorkerDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField(default=8080808080)
    profession = models.CharField(max_length=20,default="")
    pin_code = models.IntegerField(default=500005)

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField(default=8080808080)


class Bookings(models.Model):
    client_user = models.ForeignKey('UserDetails', on_delete=models.CASCADE, max_length=5)
    worker = models.ForeignKey('WorkerDetails', on_delete=models.CASCADE, max_length=5)
    address = models.CharField(max_length=30,default="no")
    booking_date = models.DateTimeField()
    booking_status = models.CharField(max_length=10)
