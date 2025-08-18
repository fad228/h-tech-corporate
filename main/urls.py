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
]
