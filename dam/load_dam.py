import os
from django.contrib.gis.utils import LayerMapping
from dam.models import Dam, DamType, Institution, Purpose
import json

mapping = {
    # Dam に定義したオブジェクト名 : geo json のキーワード
    'name': 'W01_001',  # Infraモデルで提供された名前を使う
    'dam_code': 'W01_002',
    'water_system_name': 'W01_003',
    'river_name': 'W01_004',
    'type_code': {'id': 'W01_005'},
    'purpose_code': 'W01_006',
    'scale_bank_height': 'W01_007',
    'scale_bank_span': 'W01_008',
    'bank_volume': 'W01_009',
    'total_pondage': 'W01_010',
    'institution_in_charge': {'id': 'W01_011'},
    'year_of_completion': 'W01_012',
    'address': 'W01_013',  # Infraモデルで提供された名前を使う
    'positional_information_precision': 'W01_014',
    'geom': 'Point',  # Infraモデルで提供された名前を使う

    # 　以下は Infra モデルで提供されているもの
    # ''
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
        transform=False,  # 元ファイルのデータをそのまま使いたいときFalseを指定．そうしないと `geometries` が挿入される（なんだそれ？）
        encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def load_base_data():
    dam_types = [{'id': '1', 'description': 'アーチダム'},
                 {'id': '2', 'description': 'バットレスダム'},
                 {'id': '3', 'description': 'アースダム'},
                 {'id': '4', 'description': 'アスファルトフェイシングダム'},
                 {'id': '5', 'description': 'アスファルトコアダム'},
                 {'id': '6', 'description': 'フローティングゲートダム（可動堰）'},
                 {'id': '7', 'description': '重力式コンクリートダム'},
                 {'id': '8', 'description': '重力式アーチダム'},
                 {'id': '9', 'description': '重力式コンクリートダム・フィルダム複合ダム'},
                 {'id': '10', 'description': '中空重力式コンクリートダム'},
                 {'id': '11', 'description': 'マルティプルアーチダム'},
                 {'id': '12', 'description': 'ロックフィルダム'},
                 {'id': '13', 'description': '台形CSG ダム'},
                 {'id': '-', 'description': '-'},
                 ]
    for dam_type in dam_types:
        record = DamType.create(**dam_type)
        record.save()

    institutions = [
        {'id': '1', 'name': '国土交通省（各地方整備局，北海道開発局含む）'},
        {'id': '2', 'name': '沖縄振興局（旧沖縄開発庁）'},
        {'id': '3', 'name': '農林水産省（各地方農政局含む）'},
        {'id': '4', 'name': '都道府県'},
        {'id': '5', 'name': '市区町村'},
        {'id': '6', 'name': '水資源機構（旧水資源開発公団）'},
        {'id': '7', 'name': 'その他の公共企業体  '},
        {'id': '8', 'name': '土地改良区 '},
        {'id': '9', 'name': '利水組合・用水組合 '},
        {'id': '10', 'name': '電力会社・電源開発株式会社'},
        {'id': '11', 'name': 'その他の企業'},
        {'id': '12', 'name': '個人'},
        {'id': '13', 'name': 'その他'},
        {'id': '-', 'name': '-'},
    ]

    for institution in institutions:
        record = Institution.create(**institution)
        record.save()

    purposes = [
        {'id': '1', 'name': '洪水調節，農地防災'},
        {'id': '2', 'name': '不特定用水，河川維持用水'},
        {'id': '3', 'name': '灌漑，特定(新規)灌漑用水'},
        {'id': '4', 'name': '上水道用水'},
        {'id': '5', 'name': '工業用水道用水'},
        {'id': '6', 'name': '発電'},
        {'id': '7', 'name': '消流雪用水'},
        {'id': '8', 'name': 'レクリエーション'},
        {'id': '-', 'name': '-'},
    ]

    for purpose in purposes:
        record = Purpose.create(**purpose)
        record.save()


def load_records():
    excludes = ['purpose_code','type_code','institution_in_charge']
    #load json
    with open('./dam/data/output.json', encoding='utf8') as json_file:
        records = json.load(json_file)
        for record in records:
            #keys to exclude purpose_code,type_code,institution_in_charge

            # First, create Dam record excluding fields that have many to many relationship
            record_excluded = {k: v for k, v in record.items() if k not in excludes}
            # print(record_excluded)

            dam = Dam(**record_excluded)

            # type_code - OneToMany field
            dam_type = record.get('type_code')
            dam.type_code = DamType.objects.get(pk=dam_type)

            dam.save()

            # Purpose - ManyToMany field
            purpose_codes = record.get('purpose_code')
            for purpose_code in purpose_codes.split(','):
                dam.purpose_code.add(Purpose.objects.filter(id=purpose_code)[0])

            # institution_in_charge - ManyToMany field
            institutions = record.get('institution_in_charge')
            for institution in institutions.split(','):
                dam.institution_in_charge.add(Institution.objects.filter(id=institution)[0])

            # print(dam)