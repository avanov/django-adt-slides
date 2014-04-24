from django.db import models
from .types import Language


class IRegionalArticle(models.Model):
    class Meta:
        abstract = True
    title = models.CharField(max_length=140, default='')
    text = models.TextField(max_length=65536, default='')


@Language.ENGLISH('db:articles')
class EnglishArticle(IRegionalArticle):
    pass


@Language.GERMAN('db:articles')
class GermanArticle(IRegionalArticle):
    pass
