from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('blog.urls')),

    url(r'^blog/', include('blog.urls')), # <- string
    url(r'^admin/', include(admin.site.urls)), # <- object
)
