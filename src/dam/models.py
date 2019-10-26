
# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Dam(models.Model):
    damName = models.CharField(max_length=255)
    damCode = models.IntegerField()
    waterSystemName = models.CharField(max_length=255)
    riverName = models.CharField(max_length=255)
    dam_type = models.CharField(max_length=255)
    purpose  = models.CharField(max_length=255)
    damScaleBankHeight   = models.FloatField()
    damScaleBankSpan  = models.FloatField()
    bankVolume  = models.IntegerField()
    totalPondage  = models.IntegerField()
    institutionInCharge  = models.CharField(max_length=255)
    yearOfCompletion  = models.CharField(max_length=255)
    address  = models.CharField(max_length=255)
    positionalInformationPrecision  = models.IntegerField()
    geom = models.PointField(srid=6668)

    def __str__(self):
        return self.name
    