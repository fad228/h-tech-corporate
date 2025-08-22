from django.contrib import admin
from .models import Collaborateur
from .models import VideoPublicitaire
from .models import Service
from .models import Media
# Register your models here.
from .models import Temoignage, MediaTemoignage
from .models import Produit

admin.site.register(Media)
admin.site.register(Temoignage)
admin.site.register(MediaTemoignage)
admin.site.register(Collaborateur)
admin.site.register(VideoPublicitaire)
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("nom", "prix_min", "prix_max", "contact_direction")
    list_filter = ("contact_direction",)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    search_fields = ('nom',)
