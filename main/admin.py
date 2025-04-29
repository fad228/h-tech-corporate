from django.contrib import admin

# Register your models here.
from .models import Temoignage, MediaTemoignage

admin.site.register(Temoignage)
admin.site.register(MediaTemoignage)
