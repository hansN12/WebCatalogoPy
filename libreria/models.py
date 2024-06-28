from django.db import models

# Create your models here.
class Artists(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    genre = models.CharField(max_length=50, verbose_name="Género")

    def __str__(self):
        fila = "Nombre: " + self.name + " -- " + "Género: " + self.genre
        return fila



class Albums(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Título")
    release_date = models.DateField(verbose_name="Fecha de Lanzamiento")
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, verbose_name="Artista")

    def __str__(self):
        fila = "Título: " + self.title + " -- " + "Fecha de Lanzamiento: " + str(self.release_date) + " -- " + "Artista: " + self.artist.name
        return fila
