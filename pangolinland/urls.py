from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from pangolinland.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main),
    url(r'^getebook/$', getebook),
    # url(r'article/', include('article.urls')),
    # url(r'support/', include('article.urls')),
    # url(r'news/$',news),
    # url(r'contact/$',contact),
    

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEVELOPMENT and settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)))

if settings.DEVELOPMENT or settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}))
