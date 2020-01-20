import uuid
from django.utils import timezone
from django.contrib.gis.db import models

class Category(models.Model):
	id = models.CharField(primary_key=True, max_length=2)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	@classmethod
	def create(cls, id, name):
		category = cls(id=id, name=name)
		return category

class Infra(models.Model):
	"""インフラベースモデル
	"""
	class Meta:
		# マイグレーションするときにテーブルは作成されない設定
		# よって他のモデルに継承するためのモデルになる
		abstract = True


	id = models.IntegerField(null=False, primary_key=True)
	name = models.CharField(verbose_name='名称', max_length=50)
	address = models.CharField(verbose_name='住所', max_length=60)
	category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT, blank=True, null=True)
	registered_at = models.DateTimeField(default=timezone.now)
	modified_at = models.DateTimeField(blank=True, null=True)
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
