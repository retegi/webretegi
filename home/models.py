
from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField


class Label(models.Model):
    name = models.CharField('Etiqueta', max_length=100, null=True, blank=True)
    backgroundColor = models.CharField('Color fondo', max_length=12, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"
    
    def __str__(self):
        return (self.name)


# Create your models here.
class Post(models.Model):
    title = models.TextField('Título', max_length=300, null=True, blank=True)
    datetime = models.DateTimeField('Fecha y hora', null=True, blank=True)
    resume = models.TextField('Resume', max_length=300, null=True, blank=True)
    #text = models.TextField('Texto', max_length=12000, null=True, blank=True)
    text = RichTextField()
    image = models.ImageField('Image', null=True, blank=True, upload_to="img/")
    label = models.ManyToManyField(Label, blank=True)
    author = models.CharField('Autor', max_length=30, blank=True, null=True)
    readingTime = models.IntegerField('Tiempo lectura', blank=True, null=True)

    class Meta:
        ordering = ['-datetime']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return (self.title)

class Project(models.Model):
    title = models.TextField('Título', max_length=300, null=True, blank=True)
    datetime = models.DateTimeField('Fecha y hora', null=True, blank=True)
    resume = models.TextField('Resume', max_length=300, null=True, blank=True)
    text = models.TextField('Texto', max_length=12000, null=True, blank=True)
    image = models.ImageField('Image', null=True, blank=True, upload_to="img/")

    class Meta:
        ordering = ['-datetime']
        verbose_name = "Project"
        verbose_name_plural = "Project"
    
    def __str__(self):
        return (self.title)


