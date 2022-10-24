from django.db import models

# Create your models here.
class Brandlist(models.Model):
    name = models.CharField( primary_key = True, max_length = 100) 
    category = models.CharField(max_length = 100)
    imageurl = models.CharField(max_length = 1000, default =None, null = True)
    class Meta:
        db_table = 'brandlist'


class Typelist(models.Model):
    name = models.CharField(primary_key = True, max_length = 100) 
    
    class Meta:
        db_table = 'typelist'