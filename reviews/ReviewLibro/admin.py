from django.contrib import admin
from .models import Libro,Usuario,Reseña
# Register your models here.
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Reseña)