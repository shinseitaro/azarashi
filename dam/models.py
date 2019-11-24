#from django.db import models
from infrastructure.models import Infra
from django.contrib.gis.db import models

class DamType(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    @classmethod
    def create(cls, id, description):
        dam_type = cls(id=id, description=description)
        return dam_type

class Institution(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, id, name):
        institution = cls(id=id, name=name)
        return institution

class Purpose(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, id, name):
        purpose = cls(id=id, name=name)
        return purpose

class Dam(Infra):
    dam_code = models.IntegerField(null=False)
    water_system_name = models.CharField(max_length=50)
    river_name = models.CharField(max_length=50)
    type_code = models.ForeignKey(DamType, on_delete=models.CASCADE, null=True, blank=True)
    purpose_code = models.ManyToManyField(Purpose, blank=True, null=True)
    scale_bank_height = models.FloatField()
    scale_bank_span = models.FloatField()
    bank_volume = models.IntegerField()
    total_pondage = models.IntegerField()
    institution_in_charge = models.ManyToManyField(Institution, blank=True, null=True)
    year_of_completion = models.CharField(max_length=10)
    positional_information_precision = models.IntegerField()
    geom = models.PointField(srid=4019, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)