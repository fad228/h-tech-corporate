   # Create your models here.
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Formation(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    duree = models.CharField(max_length=50)
    tarif = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titre


class Temoignage(models.Model):
    nom = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom



class Inscription(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True, null=True)
    formation = models.CharField(max_length=100)
    date_inscription = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True) 
    def __str__(self):
        return f"{self.nom} - {self.formation}"

    
    

class Temoignage(models.Model):
    nom = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nom} - {self.date.strftime('%d/%m/%Y')}"


class MediaTemoignage(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('photo', 'Photo'),
        ('video', 'Vidéo'),
    )
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)
    fichier = CloudinaryField('media') 
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.media_type} - {self.description}"
    
  

class Collaborateur(models.Model):
    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='collaborateurs/')
    poste = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom



class VideoPublicitaire(models.Model):
    titre = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True, null=True)
    lien_action = models.URLField(blank=True, null=True, help_text="Lien du bouton (ex: lien d'inscription)")
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


