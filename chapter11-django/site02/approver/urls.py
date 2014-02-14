from django.conf.urls import patterns, include, url


urlpatterns = patterns('approver.views',
    url(r'^$', 'list_tweets'),
    url(r'^review/(?P<tweet_id>\d+)', 'review_tweet'),                       
)
