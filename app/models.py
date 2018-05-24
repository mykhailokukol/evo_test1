from django.db import models

# Create your models here.
class FreezerTypes(models.Model):
    type = models.CharField(max_length=32)

    def __str__(self):
        return self.type

class Freezer(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    type = models.ManyToManyField(FreezerTypes, default=1)
    height = models.SmallIntegerField(default=100)              # cm
    color = models.CharField(max_length=32)

    clicks = models.IntegerField(default=0)

    def __str__(self):
        return ('%s %s' % (self.brand, self.model))

class TVTypes(models.Model):
    type = models.CharField(max_length=32)

    def __str__(self):
        return self.type

class TV(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    type = models.ManyToManyField(TVTypes, default=1)
    color = models.CharField(max_length=32)

    clicks = models.IntegerField(default=0)

    def __str__(self):
        return ('%s %s' % (self.brand, self.model))
