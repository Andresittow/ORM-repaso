from django.db import models

class Solicitud(models.Model):
    TIPO_SOLICITUD = [
        ('ACA','ACADEMICA'),
        ('ADA','ADMINISTRATIVA'),
        ('TEC','TECNICA'),
        ('OTR','OTRA'),
    ]

    nombre_solicitud= models.CharField(max_length=100)
    documento_identidad= models.CharField(max_length=100)
    correo_electronico= models.EmailField()
    telefono_contacto= models.CharField(max_length=100)
    tipo_solicitud = models.CharField(max_length=3,choices=TIPO_SOLICITUD,default='ACA')

    def __str__(self):
        return f"{self.nombre_solicitud} - {self.documento_identidad} - {self.correo_electronico} - {self.telefono_contacto} - {self.tipo_solicitud}"


