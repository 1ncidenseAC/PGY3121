from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    precio = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)
    activo = models.BooleanField()

class Categoria(models.Model):
    idCategoria = models.AutoField(db_column='idCategoria', primary_key=True) 
    categoria = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.categoria)