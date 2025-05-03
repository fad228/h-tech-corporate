from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        # Remplace les noms ici par les noms de tes vues nommées
        return ['home', 'about', 'formations', 'temoignages', 'inscription', 'contact', 'services']

    def location(self, item):
        return reverse(item)
