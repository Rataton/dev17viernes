from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=120, verbose_name=u'Nombre') # verbose_name es para indicar una variacion del label
    last_name = models.CharField(
        max_length=120, blank=True, null=True, verbose_name=u'Apellido'
    )
    number = models.CharField(max_length=10, verbose_name=u'Numero')
    phone_number = models.CharField(
        max_length=10, verbose_name=u'Celular', blank=True
    )
    email = models.EmailField()
    direccion = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name + ' ' + self.last_name


class Group(models.Model):
    name = models.CharField(max_length=120, verbose_name=u'Nombre')
    description = models.CharField(max_length=300, verbose_name=u'Descripcion')
    person = models.ForeignKey(Person)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
