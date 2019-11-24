import os 
from django.contrib.gis.utils import LayerMapping 
from dam.models import Dam


mapping = {
	# Dam に定義したオブジェクト名 : geo json のキーワード
	'dam_name': 'W01_001',
	'dam_code': 'W01_002',
	'water_system_name': 'W01_003', 
	'river_name': 'W01_004', 
	'type_code': 'W01_005', 
	'purpose_code': 'W01_006', 
	'scale_bank_height': 'W01_007', 
	'scale_bank_span': 'W01_008',
	'bank_volume': 'W01_009', 
	'total_pondage': 'W01_010',
	'institution_in_charge': 'W01_011', 
	'year_of_completion': 'W01_012', 
	'address': 'W01_013', 
	'positional_information_precision': 'W01_014', 
	'geom': 'Point',
}

geojson_file = os.path.abspath(
	os.path.join(
		os.path.dirname(__file__), 'data', 'dam.geojson'
	)
)


def run(verbose=True):
	# LayerMapping．ベクターデータ（shape file など）を地図上にマップする方法を提供してくれる．ここでは geojson ファイルのデータをDBにロードする．
	lm = LayerMapping(
		Dam,
		geojson_file,
		mapping,
		transform=False, # 元ファイルのデータをそのまま使いたいときFalseを指定．そうしないと `geometries` が挿入される（なんだそれ？）
		encoding='UTF-8')
	lm.save(strict=True, verbose=verbose)

    