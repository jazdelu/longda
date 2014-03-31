from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contact.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cn/$', 'contact.views.home', name='cn_home'),
    url(r'^en/$', 'contact.views.en_home', name='en_home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sendmail/', 'contact.views.sendmail',name = 'sendmail'),
)

urlpatterns += staticfiles_urlpatterns()