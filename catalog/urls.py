from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^catalog/$', views.catalog_all, name='catalog'),
    url(r'^kruzhevo/$', views.kruzhevo, name='kruzhevo'),
    url(r'^kruzhevo/elastichnoe$', views.elastichnoe, name='elastichnoe'),
    url(r'^kruzhevo/na_setke$', views.na_setke, name='na_setke'),
    url(r'^kruzhevo/s_resnichkami$', views.s_resnichkami, name='s_resnichkami'),
    url(r'^kruzhevo/polotno$', views.polotno, name='polotno'),
    url(r'^kruzhevo/shantili$', views.shantili, name='shantili'),
    url(r'^elastichnaja_tesma/$', views.elastichnaja_tesma, name='elastichnaja_tesma'),
    url(r'^elastichnaja_tesma/breteli$', views.breteli, name='breteli'),
    url(r'^elastichnaja_tesma/kosaja_bejka$', views.kosaja_bejka, name='kosaja_bejka'),
    url(r'^elastichnaja_tesma/tonnelnaja_lenta$', views.tonnelnaja_lenta, name='tonnelnaja_lenta'),
    url(r'^elastichnaja_tesma/believye_rezinki$', views.believye_rezinki, name='believye_rezinki'),
    url(r'^furnitura/$', views.furnitura, name='furnitura'),
    url(r'^furnitura/krjuchki$', views.krjuchki, name='krjuchki'),
    url(r'^furnitura/zastezhki$', views.zastezhki, name='zastezhki'),
    url(r'^furnitura/kostochki$', views.kostochki, name='kostochki'),
    url(r'^furnitura/believoj_paralon$', views.believoj_paralon, name='believoj_paralon'),
    url(r'^prochee/$', views.prochee, name='prochee'),
    url(r'^prochee/dekorativnye_elementy$', views.dekorativnye_elementy, name='dekorativnye_elementy'),
]
