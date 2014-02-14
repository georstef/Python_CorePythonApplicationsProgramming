from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site02.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('poster.urls')),
    url(r'^post/', include('poster.urls')),
    url(r'^approve/', include('approver.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # in order for the next url to work copy base.html and login.html
    # to <python_folder>\Lib\site-packages\django\contrib\admin\templates
    url(r'^login/', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout', 'django.contrib.auth.views.logout'),
)
