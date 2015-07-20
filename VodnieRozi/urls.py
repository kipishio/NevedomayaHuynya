#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VodnieRozi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

     url(r'^', include('KatalogCvetov.urls', namespace='KatalogCvetov')),
     url(r'^qwe/', include('KatalogCvetov.urls')),
    # url(r'^ssilkirosteniy/', include('KatalogCvetov.urls')),
     url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
