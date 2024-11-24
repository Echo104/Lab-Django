from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    user = models.CharField(max_length=30)

class Reseña(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calificacion = models.IntegerField() 
    comentario = models.TextField()

    def __str__(self):
        return f'Reseña de {self.usuario} para {self.libro}'