from django.db import models

# Create your models here.
class Crop(models.Model):
    domain_code = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    area_code = models.IntegerField()
    area = models.CharField(max_length=100)
    element_code = models.IntegerField()
    element = models.CharField(max_length=100)
    item_code = models.IntegerField()
    item = models.CharField(max_length=100)
    year_code = models.IntegerField()
    year = models.IntegerField()
    unit = models.CharField(max_length=100)
    value = models.FloatField()
    flag = models.BooleanField()
    flag_description = models.CharField(max_length=100)
