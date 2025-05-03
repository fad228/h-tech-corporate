from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        # Remplace les noms ici par les noms de tes vues nommées
        return ['home', 'about', 'formations', 'temoignages', 'inscription_view', 'contact_view', 'services']

    def location(self, item):
        return reverse(item)
