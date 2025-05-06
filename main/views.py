from django.shortcuts import render,get_object_or_404, redirect
from .models import Formation, Temoignage
from .forms import InscriptionForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import TemoignageForm
from .models import Collaborateur
from .models import VideoPublicitaire


def home(request):
    formations = Formation.objects.all()[:3]
    temoignages = Temoignage.objects.all()[:2]
    video = VideoPublicitaire.objects.last()
    return render(request, 'main/home.html', {'formations': formations, 'temoignages': temoignages, 'video': video})


def about(request):
    collaborateurs = Collaborateur.objects.all()
    return render(request, 'main/about.html', {'collaborateurs': collaborateurs})


def formations(request):
    formations = Formation.objects.all()
    return render(request, 'main/formations.html', {'formations': formations})


from .models import Temoignage, MediaTemoignage

def temoignages(request):
    temoignages = Temoignage.objects.order_by('-date')
    medias = MediaTemoignage.objects.all()
    if request.method == 'POST':
        form = TemoignageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('temoignages')
    else:
        form = TemoignageForm()
    return render(request, 'main/temoignages.html', {
        'form': form,
        'temoignages': temoignages,
        'medias': medias,
    })


def supprimer_temoignage(request, id):
    temoignage = get_object_or_404(Temoignage, id=id)
    if request.method == 'POST':
        temoignage.delete()
        messages.success(request, "Témoignage supprimé avec succès.")
        return redirect('temoignages')  # Redirige vers la page des témoignages



def services(request):
    return render(request, 'main/services.html')


def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # Enregistrer dans la base de données si nécessaire
            inscription = form.save()

            # --- Email à l'administrateur ---
            subject = 'Nouvelle inscription à une formation'
            message = (
                f"Nom: {form.cleaned_data['nom']}\n"
                f"Téléphone: {form.cleaned_data.get('telephone', 'non fourni')}\n"
                f"Email: {form.cleaned_data['email']}\n"
                f"Formation: {form.cleaned_data['formation']}\n"
            )
            admin_email = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email], fail_silently=False)

            # --- Message à l'utilisateur ---
            messages.success(request, 'Votre inscription a bien été envoyée !')

            # Redirection vers un lien WhatsApp avec infos préremplies
            return redirect(
                f"https://wa.me/22898700015?text=Nouvelle%20inscription%20de%20{form.cleaned_data['nom']}%20pour%20la%20formation%20{form.cleaned_data['formation']}"
            )
    else:
        form = InscriptionForm()
    return render(request, 'main/inscription.html', {'form': form})

# views.py


def contact_view(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        sujet = f"Message de {nom} via le site H-Tech Corporate"
        contenu = f"Nom : {nom}\nEmail : {email}\n\nMessage :\n{message}"

        try:
            send_mail(
                sujet,
                contenu,
                settings.DEFAULT_FROM_EMAIL,
                ["fadilekpaye@email.com"],  # Remplace par ton adresse email
                fail_silently=False,
            )
            messages.success(request, "Votre message a bien été envoyé.")
            return redirect('contact')
        except:
            messages.error(request, "Une erreur s'est produite. Veuillez réessayer.")

    return render(request, 'main/contact.html')





