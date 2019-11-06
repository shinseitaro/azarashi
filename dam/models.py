#from django.db import models
from infrastructure.models import Infra
from django.contrib.gis.db import models
	
class Dam(Infra):
    class Meta:
        db_table = 'dam'

    dam_code = models.IntegerField()
    water_system_name = models.CharField(max_length=50)
    river_name = models.CharField(max_length=50)
    type_code = models.CharField(max_length=20)
    purpose_code = models.CharField(max_length=20)
    scale_bank_height = models.FloatField()
    scale_bank_span = models.FloatField()
    bank_volume = models.IntegerField()
    total_pondage = models.IntegerField()
    institution_in_charge = models.CharField(max_length=20)
    year_of_completion = models.CharField(max_length=10)
    positional_information_precision = models.IntegerField()

	# この3つは，Infraで提供されるので，不要
    #dam_name = models.CharField(max_length=50)
    #address = models.CharField(max_length=50)
    #geom = models.PointField(srid=4019)	

    def __str__(self):
        return self.name
