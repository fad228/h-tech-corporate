from django.shortcuts import render,get_object_or_404, redirect
from .models import Formation, Temoignage
from .forms import InscriptionForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import TemoignageForm
from .models import Collaborateur
from .models import VideoPublicitaire
from .models import Service, DemandeService
from .forms import DemandeServiceForm
from .models import Media


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
                ["htechcorporatetogo@gmail.com"],  # Remplace par ton adresse email
                fail_silently=False,
            )
            messages.success(request, "Votre message a bien été envoyé.")
            return redirect('contact')
        except:
            messages.error(request, "Une erreur s'est produite. Veuillez réessayer.")

    return render(request, 'main/contact.html')



def service(request):
    service = Service.objects.all()
    form = DemandeServiceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        
        service_nom = form.cleaned_data['service']
        nom = form.cleaned_data['nom_utilisateur']
        email = form.cleaned_data['email']
        telephone = form.cleaned_data['telephone']

        send_mail(
            subject="Nouvelle demande de service",
            message=f"Service demandé : {service_nom}\nNom : {nom}\nEmail : {email}\nTéléphone : {telephone}",
            from_email='htechcorporatetogo@gmail.com',
            recipient_list=['htechcorporatetogo@gmail.com'],  # ton email ici
            fail_silently=False,
        )

        messages.success(request, "Votre demande a été envoyée avec succès.")
        return redirect('prestation') 
    return render(request, 'main/service.html', {'service': service, 'form': form})

    

def galerie(request):
    medias = Media.objects.all()
    return render(request, 'main/galerie.html', {'medias': medias})


# views.py
from django.shortcuts import render, get_object_or_404
from .models import Produit

def boutique(request):
    produits = Produit.objects.all()
    return render(request, "boutique/boutique.html", {"produits": produits})

def produit_detail(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, "boutique/detail.html", {"produit": produit})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit



# Supprimer un produit du panier
def supprimer_du_panier(request, produit_id):
    panier = request.session.get('panier', {})
    if str(produit_id) in panier:
        del panier[str(produit_id)]
        request.session['panier'] = panier
    return redirect('panier')



from django.shortcuts import get_object_or_404, redirect, render
from .models import Produit
from django.contrib import messages
from django.utils.http import urlencode


def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    panier = request.session.get('panier', {})

    if str(produit_id) in panier:
        panier[str(produit_id)]['quantite'] += 1
    else:
        panier[str(produit_id)] = {
            'nom': produit.nom,
            'prix': float(produit.prix),
            'quantite': 1,
            'image': produit.image.url if produit.image else ""
        }

    request.session['panier'] = panier
    request.session.modified = True

    messages.success(request, f"{produit.nom} ajouté au panier !")
    return redirect('boutique')


def panier(request):
    panier = request.session.get('panier', {})
    total = 0
    message_whatsapp = "Bonjour, je souhaite commander :\n"

    for item in panier.values():
        sous_total = item['prix'] * item['quantite']
        total += sous_total
        message_whatsapp += f"- {item['nom']} (x{item['quantite']})\n"

    message_whatsapp += f"\nTotal : {total} FCFA"

    # ⚠️ Mets ton vrai numéro WhatsApp ici (format international, ex: 22891234567)
    whatsapp_number = "22892542889"
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text=" + urlencode({'': message_whatsapp})[1:]

    return render(request, 'boutique/panier.html', {
        'panier': panier,
        'total': total,
        'whatsapp_url': whatsapp_url
    })


def modifier_quantite(request, key):
    if request.method == "POST":
        quantite = int(request.POST.get('quantite', 1))
        panier = request.session.get('panier', {})
        if key in panier:
            panier[key]['quantite'] = quantite
            panier[key]['total'] = panier[key]['prix'] * quantite
            request.session['panier'] = panier
    return redirect('panier')
