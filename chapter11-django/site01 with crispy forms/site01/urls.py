from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    #next 2 lines have the same result, the 2nd with redirect to 
    #url(r'^$', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='/blog/')),

    url(r'^blog/', include('blog.urls')), # <- string
    url(r'^admin/', include(admin.site.urls)), # <- object
)
