import uuid 
#from django.db import models 
from django.utils import timezone 
from django.contrib.gis.db import models


class Category(models.Model):
	name = models.CharField(max_length=50)


class Infra(models.Model):
	"""インフラベースモデル
	"""
	class Meta: 
		db_table = 'infra' 
		
		# マイグレーションするときにテーブルは作成されない設定
		# よって他のモデルに継承するためのモデルになる
		abstract = True 
		

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(verbose_name='名称', max_length=50)
	address = models.CharField(verbose_name='住所', max_length=50)
	category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
	registered_at = models.DateTimeField(default=timezone.now)
	modified_at = models.DateTimeField(blank=True, null=True)
	# https://docs.djangoproject.com/en/2.2/ref/models/fields/#urlfield
	url = models.URLField(blank=True)

	geom = models.PointField(srid=4019) 
	
	# card はいったん保留
	#card = models.ManyToManyField()
	
	def modified(self):
		self.modified_at = timezone.now() 
		self.save()

	def __str__(self):
		return self.name 


# class Card(models.Model):
# 	"""
# 	ToDO ここからです．
# 	"""
# 	publisher = ''
# 	distributer = ''
# 	is_official = ''
# 	is_unofficial = ''
# 	version = ''
# 	availability = ''

# 	# card 独自のURLを持っているときがあるので．周年記念カード紹介サイトとか．
# 	url = models.URLField(blank=True)



# class Dam(models.Model):
# 	"""ダムクラス""" 

# 	class Meta:
# 		db_table = 'dam'
	
