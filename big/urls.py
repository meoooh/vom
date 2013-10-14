from django.conf.urls import patterns, include, url
from vom.views import *
from django.conf.urls.static import static
from django.conf import settings
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

_static = os.path.join(os.path.dirname(__file__), 'static')

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    # url(r'^big/', include('big.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^djemals/', include(admin.site.urls)),
    url(r'^login/?$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/?$', 'django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'^answers/?$', createAnswer, name='createAnswer'),
    # url(r'^questions/?$', questions, name='questions'),
    url(r'^questions/(?P<pk>[^/]+)/?$', showAnswer, name='showAnswer'),
    url(r'^join/?$', join, name='join'),
    url(r'^_static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': _static}),
    url(r'setting/?$', cogwheel, name='setting'),
    url(r'constellations/(?P<name>[^/]+)/?$', showConstellation,
        name='showConstellation'),
    url(r'constellations/(?P<name>[^/]+)/(?P<pk>[\d]+)/?$',
        showConstellationRelatedQuestion,
        name='showConstellationRelatedQuestion'),
    url(r'constellations/?$', stars, name='constellations'),
    url(r'today/?$', createAnswer, name='today'),
    url(r'test$', test),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)