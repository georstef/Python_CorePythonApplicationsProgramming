from django.conf.urls import patterns, include, url


urlpatterns = patterns('poster.views',
    url(r'^$', 'post_tweet'),
    url(r'^thankyou/', 'thank_you'),
    url(r'^edit/(?P<tweet_id>\d+)', 'post_tweet'),
    url(r'^del/(?P<tweet_id>\d+)', 'delete_tweet'),
    url(r'^del', 'delete_tweet'),
)
