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
    water_system_name = models.CharField(max_length=50, blank=True, null=True)
    river_name = models.CharField(max_length=50, blank=True, null=True)
    type_code = models.ForeignKey(DamType, on_delete=models.CASCADE, null=True, blank=True)
    purpose_code = models.ManyToManyField(Purpose, blank=True)
    scale_bank_height = models.FloatField(blank=True, null=True)
    scale_bank_span = models.FloatField(blank=True, null=True)
    bank_volume = models.IntegerField(blank=True, null=True)
    total_pondage = models.IntegerField(blank=True, null=True)
    institution_in_charge = models.ManyToManyField(Institution, blank=True)
    year_of_completion = models.CharField(max_length=10, blank=True, null=True)
    positional_information_precision = models.IntegerField(blank=True, null=True)
    geom = models.PointField(srid=4019, blank=True, null=True)
    prefecture = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class DamCardDistributionPlaceQuerySet(models.QuerySet):
    def filter_active(self):
        return self.filter(dam__isnull=False)


class DamCardDistributionPlaceQueryManager(
        models.Manager.from_queryset(DamCardDistributionPlaceQuerySet)):
    pass

class DamCardDistributionPlace(models.Model):
    objects = DamCardDistributionPlaceQueryManager()
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=50)
    url = models.URLField()
    address = models.CharField(max_length=100)
    operation_hour = models.CharField(max_length=200)
    prefecture = models.CharField(max_length=4)
    dam = models.ManyToManyField(Dam, blank=True)
    mon = models.BooleanField(default=False)
    tue = models.BooleanField(default=False)
    wed = models.BooleanField(default=False)
    thu = models.BooleanField(default=False)
    fri = models.BooleanField(default=False)
    sat = models.BooleanField(default=False)
    sun = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    @classmethod
    def create(cls, id, name, url, address, operation_hour, prefecture, dam):
        return cls(id=id, name=name, url=url, address=address,
                   operation_hour=operation_hour, prefecture=prefecture,
                   dam_id=dam)
