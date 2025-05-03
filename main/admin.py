from django.contrib import admin
from .models import Collaborateur
from .models import VideoPublicitaire

# Register your models here.
from .models import Temoignage, MediaTemoignage

admin.site.register(Temoignage)
admin.site.register(MediaTemoignage)
admin.site.register(Collaborateur)
admin.site.register(VideoPublicitaire)
