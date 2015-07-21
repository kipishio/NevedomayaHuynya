#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib import admin

from KatalogCvetov import views
from django.conf import settings

urlpatterns = patterns('',
    # ex: /polls/

    url(r'^$', views.index, name='index'),
    url(r'^test/', views.test, name='test'),
    url(r'^katalog/$', views.katalog, name='katalog'),
    url(r'^kontakti/$', views.kontakti, name='kontakti'),
    url(r'^onas/$', views.onas, name='onas'),
    url(r'^katalog/rastenie/(\d+)/$', views.rastenie, name='rastenie'),
    url(r'^katalog/vidrasteniya/(\d+)/$', views.vidrasteniya, name='vidrasteniya'),
    url(r'^katalogcvetov/ssilkirosteniy/(?P<katalogcvet_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<cvetok_id>\d+)/(?P<reyting_id>\d+)/(?P<kommentari_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<cvetikatalog_id>\d+)/vote/$', views.vote, name='vote'),
    # url(r'^katalogcvetov/ssilkirosteniy/$', views.ssilkirosteniy, name='ssilkirosteniy'),
    # ex: /polls/5/
    # ex: /polls/5/results/
    # ex: /polls/5/vote/

)

# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()