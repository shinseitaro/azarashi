import os 
from django.contrib.gis.utils import LayerMapping
from map.models import Hoikusho

"""
hoikusho,geojson のデータは
{
   "type": "FeatureCollection",
   "features": [
  {
    "type": "Feature",
    "geometry": {
       "type": "Point",
       "coordinates":  [ 139.777421,35.699016 ]
    },
    "properties": {
    "owned":"区市町村",
    "name":"いずみこども園",
    "postalcode":"101-0024",
    "address":"千代田区神田和泉町１",
    "gcs":"JGD2011",
    "tel":"03-3866-9938",
    "capacity":36
    }
  },

そして，モデルは

class Hoikusho(models.Model):
    owned = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    gcs = models.CharField(max_length=10)
    tel = models.CharField(max_length=50)
    capacity = models.IntegerField()
    geom = models.PointField(srid=6668)

よって，下のようにmapping を作成
"""

mapping = {
	# モデルの変数名 : データのキーワード と思っていたんだけど
	# "geom": "Point" はそれでは説明できない．どういうこと？
	"owned": "owned", 
	"name": "name", 
	"postalcode": "postalcode",
	"address": "address", 
	"gcs": "gcs", 
	"tel": "tel", 
	"capacity": "capacity", 
	"geom": "Point", 
	
}

# `201810-2-1-hoikusyo.geojson` へのファイルパス
geojson_file = os.path.abspath(
	os.path.join(
		os.path.dirname(__file__), 'data', '201810-2-1-hoikusyo.geojson'
	)
)

# 実行
def run(verbose=True):
	lm = LayerMapping(
		Hoikusho, 
		geojson_file,
		mapping, 
		transform=False, 
		encoding='UTF-8',)
	lm.save(strict=True, verbose=verbose)
	

