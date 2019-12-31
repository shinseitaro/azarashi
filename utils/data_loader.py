from dam.models import Dam, DamType, Institution, Purpose, DamCardDistributionPlace
from infrastructure.models import Category
from django.contrib.gis.geos import GEOSGeometry
import json
import csv
import traceback

def load_base_data():
    dam_types = [
        {'id': '1', 'description': 'アーチダム'},
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

    categories = [
        {'id': '1', 'name': 'ダム'}
    ]

    records = []
    for dam_type in dam_types:

        record = DamType.create(**dam_type)
        records.append(record)
    DamType.objects.bulk_create(records)

    records = []
    for institution in institutions:
        record = Institution.create(**institution)
        records.append(record)
    Institution.objects.bulk_create(records)

    records = []
    for purpose in purposes:
        record = Purpose.create(**purpose)
        records.append(record)
    Purpose.objects.bulk_create(records)

    records = []
    for category in categories:
        record = Category.create(**category)
        records.append(record)
    Category.objects.bulk_create(records)


def load_geometry():
    with open('./data/dam.geometry.csv', newline='') as file:
        rows = csv.reader(file, delimiter=',')
        next(rows)  # skip header
        dams =[]
        for row in rows:
            dam = Dam.objects.filter(dam_code=row[1])[0]
            dam.geom = GEOSGeometry(row[2])
            dams.append(dam)
        Dam.objects.bulk_update(dams, fields=['geom'])


def load_records():
    excludes = ['purpose_code', 'type_code', 'institution_in_charge']
    # load json
    with open('./data/dam.json', encoding='utf8') as json_file:
        records = json.load(json_file)

        dams = []
        for record in records:
            # keys to exclude purpose_code,type_code,institution_in_charge

            # First, create Dam record excluding fields that have many-to-many relationship
            record_excluded = {k: v for k, v in record.items() if k not in excludes}

            # dam = Dam(**record_excluded)
            dam = Dam.objects.filter(dam_code=record_excluded.get('dam_code')).first()

            if dam:
                for key, value in record_excluded.items():
                    setattr(dam, key, value) #実質的なupdate
            else:
                # type_code and category - OneToMany field
                dam = Dam(**record_excluded)
                dam_type = record.get('type_code')
                dam.type_code = DamType.objects.get(pk=dam_type)
                dam.category = Category.objects.get(pk='1')

            dam.save()

            # Purpose - ManyToMany field
            purpose_codes = record.get('purpose_code')
            for purpose_code in purpose_codes.split(','):
                dam.purpose_code.add(Purpose.objects.filter(id=purpose_code)[0])

            # institution_in_charge - ManyToMany field
            institutions = record.get('institution_in_charge')
            for institution in institutions.split(','):
                dam.institution_in_charge.add(Institution.objects.filter(id=institution)[0])

def to_boolean(val):
    return False if val == '0' else True

def load_dam_card_distribution_place():
    excludes = ['idx', 'dam', 'dam_name', 'mon','tue','wed','thu','fri','sat','sun']
    with open('./data/dam_card_places_set_editmode.csv', newline='') as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        next(reader)  # skip header
        rows = []
        for row in reader:
            rows.append(row)

        for row in rows:
            place = DamCardDistributionPlace.objects.filter(id=row['id'])
            if not place:
                row_excluded = {k: v for k, v in row.items() if k not in excludes}
                try:
                    place = DamCardDistributionPlace(**row_excluded)
                    place.save()

                    if row['dam'] == '':
                        continue
                    dam_to_be_added = Dam.objects.filter(dam_code=int(row['dam']))
                    if dam_to_be_added is not None:
                       place.dam.add(dam_to_be_added[0])

                except Exception:
                    print(row)
                    print(traceback.format_exc())

        #営業曜日の追加
        places = []
        for row in rows:
            place = DamCardDistributionPlace.objects.get(id=row['id'])
            place.mon = to_boolean(row['mon'])
            place.tue = to_boolean(row['tue'])
            place.wed = to_boolean(row['wed'])
            place.thu = to_boolean(row['thu'])
            place.fri = to_boolean(row['fri'])
            place.sat = to_boolean(row['sat'])
            place.sun = to_boolean(row['sun'])
            places.append(place)
        DamCardDistributionPlace.objects.bulk_update(places, fields=['mon','tue','wed','thu','fri','sat','sun'])



def run():
    print('starting...')
    load_base_data() #先にpurpose, dam_type, institutionのテーブルを作成
    print('loaded base data...loading dam data')
    load_records() #データを読み込み、dbに投入
    print('loaded dam data...loading geometry data')
    load_geometry() #geometry項目はgeopandasのdataframe->json化できなかったので、csv化した
    print('load dam card distribution place...')
    load_dam_card_distribution_place()
    print('all done! you are good to go! Create user and Do python manage.py runserver --settings [your env config]!')

if __name__ == '__main__':
    run()
