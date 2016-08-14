from __future__ import unicode_literals

from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=10)
    breed = models.ForeignKey(Breed)

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.breed.name)