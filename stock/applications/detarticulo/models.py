from django.db import models
from django.core.validators import MinValueValidator
from applications.articulo.models import Articulo
class Detarticulo(models.Model):
    nombre=models.ForeignKey(Articulo, on_delete= models.CASCADE, default=None )
    fecha=models.CharField(max_length=50)
    observacion=models.CharField(max_length=50)
    cantidad=models.IntegerField(default=0,validators=[MinValueValidator(0)])
# Create your models here.
