from django.conf import settings
from django.db import models
from dam.models import Dam


class Card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(blank=False, null=False)
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    dam = models.ForeignKey(Dam, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
