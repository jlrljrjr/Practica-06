from django.db import models

# Create your models here.
class Refresco(models.Model):
    nombre=models.CharField(max_length=20)
    sabor=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    presentacion=models.CharField(max_length=20, choices=[("botella","botella"),("lata","lata"),("botella mini","botella mini")])
    fecha_creado=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.marca}-{self.fecha_creado}"
    
    