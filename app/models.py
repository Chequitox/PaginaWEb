from django.db import models

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length= 200)
    descripcion = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank = True, default= True)
    image= models.ImageField(upload_to="media", blank=True, null=True)

    def __str__(self):
        return self.titulo