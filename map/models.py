from django.db import models

from django.contrib.gis.db import models

class Hoikusho(models.Model):
    owned = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    gcs = models.CharField(max_length=10)
    tel = models.CharField(max_length=50)
    capacity = models.IntegerField()
    geom = models.PointField(srid=6668)

def __str__(self):
    return self.name