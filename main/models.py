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
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    fichier = CloudinaryField('media', resource_type='auto')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.media_type} - {self.description}"
    
class video(models.Model):
    titre = models.CharField(max_length=100)
    fichier = CloudinaryField('video', resource_type='video')

class Collaborateur(models.Model):
    nom = models.CharField(max_length=100)
    fichier = CloudinaryField('media', resource_type='image')
    poste = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom




class VideoPublicitaire(models.Model):
    titre = models.CharField(max_length=200)
    fichier = CloudinaryField('media', resource_type='video')  # attention : pas de 'media' ici
    description = models.TextField(blank=True, null=True)
    lien_action = models.URLField(blank=True, null=True, help_text="Lien du bouton (ex: inscription)")
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre




class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    prix_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contact_direction = models.BooleanField(default=False)
    def __str__(self):
        return self.nom

    @property
    def prix_affiche(self):
        
        if self.contact_direction:
            return "Veuillez contacter la direction pour plus d'informations"
        elif self.prix_min and self.prix_max:
            return f"{self.prix_min:,} – {self.prix_max:,} FCFA"
        elif self.prix_min:
            return f"À partir de {self.prix_min:,} FCFA"
        else:
            return "Prix non défini"




class DemandeService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    nom_utilisateur = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_utilisateur} - {self.service.nom}"
