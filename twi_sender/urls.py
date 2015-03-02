from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twi_sender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
# Serve media files through Django if in debug mode
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.views',
        url(r'%s(?P<path>.*)$' % settings.MEDIA_URL[1:], "static.serve", {
            'document_root': settings.MEDIA_ROOT
        })
    )