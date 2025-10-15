from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from techmcq.models import TechMCQ,Category




class TestSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return TechMCQ.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on1


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['index','searchtoolsjobs','suscribe','contactus',
                'about_us',
                'learnfree','jobs','engineering',
                'business','sales','communication','privacy_policy',
                'mcq','downloadapp', 'ushort',]

    def location(self, item):
        return reverse(item)