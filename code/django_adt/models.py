from django.db import models


class Order(models.Model):
     tid = models.IntegerField()
     price = models.DecimalField(max_digits=16, decimal_places=4)
     size = models.IntegerField()


class Cancel(models.Model):
    xtid = models.IntegerField()


class CancelReplace(models.Model):
    xr_tid = models.IntegerField()
    new_price = models.DecimalField(max_digits=16, decimal_places=4)
    new_size = models.IntegerField()
