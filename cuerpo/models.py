from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    """
    Modelo para almacenar posts
    """

    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 200)
    texto = models.TextField()

    fechaCreacion = models.DateTimeField(
        default= timezone.now()

    )

    fechaPublicacion = models.DateTimeField(
        blank = True, null = True
    )

    def publicar(self):
        """
        El metodo para obtener la fecha de publicacion cuando se publique algun post, no el metodo post
        """
        self.fechaPublicacion = timezone.now()
        self.save()

    #Metodo mágico que nos permite castear un objeto a una cadena

    def _str_(self):
        return self.titulo