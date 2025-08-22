from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('formations/', views.formations, name='formations'),
    path('temoignages/', views.temoignages, name='temoignages'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact_view, name='contact'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('temoignage/supprimer/<int:id>/', views.supprimer_temoignage, name='supprimer_temoignage'),
    path('service/', views.service, name='prestation'),
    path('galerie/', views.galerie, name='galerie'),
    path("boutique/", views.boutique, name="boutique"),
    path("produit/<int:produit_id>/", views.produit_detail, name="produit_detail"),
    path('supprimer/<int:produit_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('panier/modifier/<str:key>/', views.modifier_quantite, name='modifier_quantite'),
    path('ajouter-au-panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.panier, name='panier'),

]
