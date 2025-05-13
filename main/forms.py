from django import forms
from .models import Inscription
from .models import Temoignage
from .models import DemandeService

FORMATION_CHOICES = [
    ('', 'Choisissez une formation...'),
    ('archicad', 'ArchiCAD'),
    ('autocad', 'AutoCAD'),
    ('robot', 'Robot Structural Analysis'),
    ('lumion', 'Lumion'),
    ('3dsmax', '3DS Max'),
    ('covadis', 'Covadis'),
    ('excel', 'Excel'),
    ('word', 'Word'),
    ('powerpoint', 'PowerPoint'),
]


class InscriptionForm(forms.ModelForm):  # <- ici on change Form en ModelForm
    class Meta:
        model = Inscription
        fields = ['nom', 'email', 'telephone', 'formation', 'message']
        labels = {
            'nom': 'Nom complet',
            'email': 'Email',
            'telephone': 'Téléphone',
            'formation': 'Formation souhaitée',
            'message': 'Message (optionnel)',
        }

    # Optionnel : si tu veux garder les mêmes choix de formation ici :
    formation = forms.ChoiceField(choices=FORMATION_CHOICES, label='Formation souhaitée')



class TemoignageForm(forms.ModelForm):
    class Meta:
        model = Temoignage
        fields = ['nom', 'message']




class DemandeServiceForm(forms.ModelForm):
    class Meta:
        model = DemandeService
        fields = ['service', 'nom_utilisateur', 'email', 'telephone']
from django import forms
from .models import DemandeService


