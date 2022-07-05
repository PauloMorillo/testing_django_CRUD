from django.db import models


# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    identification_number = models.IntegerField()
    session_id = models.IntegerField()
    bot_id = models.IntegerField()


