from django.conf.urls import *
import blog.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', blog.views.archive),# <- view function
    url(r'^create', blog.views.create_blogpost),# <- view function
    url(r'^base', blog.views.base_template),# <- view function
)

'''
# another way (without import blog.views)
urlpatterns = patterns('blog.views',
    # Examples:
    url(r'^$', archive),# <- object 
    url(r'^create', create_blogpost),# <- callable object (or lambda function)
)
'''
