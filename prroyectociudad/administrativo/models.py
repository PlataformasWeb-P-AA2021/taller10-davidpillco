from django.db import models

# Create your models here.

# Create your models here.
class Parroquia(models.Model):
    # Opciones para el tipo de parroquia
    opciones_tipo = (
        ('rural','Parroquia rural'),
        ('urbana','Parroquia Urbana'),
        )
    # Entidades de Parroquia
    nombre = models.CharField(max_length=30)
    tipo_parroquia = models.CharField(max_length=30, \
            choices=opciones_tipo) 
    
    def __str__(self):
        return "%s - %s" % (self.nombre, 
                self.tipo_parroquia)


class Barrio (models.Model):
    # Opciones para el numero de parques
    opciones_parques = (
        (1,'Un parque'),
        (2,'Dos parques'),
        (3,'Tres parques'),
        (4,'Cuatro parques'),
        (5,'Cinco parques'),
        (6,'Seis parques'),
        )
    # Entidades de Barrio
    nombre = models.CharField(max_length=30)
    num_viviendas = models.IntegerField("Número de Viviendas")
    num_parques = models.IntegerField("Número de parques",
            choices=opciones_parques) 
    num_edificios = models.IntegerField("Número de Edificios")
    parroquia = models.ForeignKey(Parroquia, related_name='lasparroquias',
        on_delete=models.CASCADE )

    def __str__(self):
        return "%s - %s - %s - %d - %s" % (self.nombre, 
                self.num_viviendas,
                self.num_parques,
                self.num_edificios,
                self.parroquia)

