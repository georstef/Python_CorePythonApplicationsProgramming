from datetime import datetime
from django import forms
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from twython import Twython
from site02 import settings
from poster.views import *
from poster.models import Tweet, Comment

@permission_required('poster.can_approve_or_reject_tweet', login_url='/login')
def list_tweets(request):
    pending_tweets = Tweet.objects.filter(state='pending').order_by('created_at')
    published_tweets = Tweet.objects.filter(state='published').order_by('-published_at')
    return render(request, 'list_tweets.html',
                  {'pending_tweets': pending_tweets,
                   'published_tweets': published_tweets})
    pass

class ReviewForm(forms.Form):
    new_comment = forms.CharField(max_length=300,
                                  widget=forms.Textarea(attrs={'cols':50,'rows':6}),
                                  required=False)
    APPROVAL_CHOICES = (
        ('approve', 'Approve this tweet and post it online'),
        ('reject', 'Reject this tweet and send it back to the author')
        )
    approval = forms.ChoiceField(choices=APPROVAL_CHOICES, widget=forms.RadioSelect)

@permission_required('poster.can_approve_or_reject_tweet', login_url='/login')
def review_tweet(request, tweet_id):
    reviewed_tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_comment = form.cleaned_data['new_comment']
            if form.cleaned_data['approval'] == 'approve':
                publish_tweet(reviewed_tweet)
                #send_approval_email(reviewed_tweet, new_comment)
                reviewed_tweet.published_at = datetime.now()
                reviewed_tweet.state = 'published'
            else:
                link = request.build_absolute_uri(
                    reverse(post_tweet, args=[reviewed_tweet.id]))
                #send_rejection_email(reviewed_tweet, new_comment, link)
                reviewed_tweet.state = 'published'
            reviewed_tweet.save()
            if new_comment:
                c = Comment(tweet=reviewed_tweet, text=new_comment)
                c.save()
            return HttpResponseRedirect('/approve/')
    else:
        form = ReviewForm()
    return render(request, 'review_tweet.html',
                  {'form': form,
                   'tweet': reviewed_tweet,
                   'comments': reviewed_tweet.comment_set.all()}
                  )

def send_approval_email(tweet, new_comment):
    body = ['Your tweet ({0}) was approved and published'.format(tweet.text)]
    if new_comment:
        body.append('You also had this {0} feedback'.format(new_comment))
        send_mail('Tweet published',
                  '\r\n'.join(body),# add into a single string all lines of the list
                  settings.DEFAULT_FROM_EMAIL,
                  [tweet.author_email])
                
def send_rejection_email(tweet, new_comment, link):
    body = ['Your tweet ({0}) was rejected'.format(tweet.text)]
    if new_comment:
        body.append('You also had this {0} feedback'.format(new_comment))
        body.append('To edit your tweet go to {0}'.format(link))
        send_mail('Tweet rejected',
                  '\r\n'.join(body),# add into a single string all lines of the list
                  settings.DEFAULT_FROM_EMAIL,
                  [tweet.author_email])

def publish_tweet(tweet):
    twitter = Twython(
        settings.TWITTER_CONSUMER_KEY,
        settings.TWITTER_CONSUMER_SECRET,
        settings.TWITTER_OAUTH_TOKEN,
        settings.TWITTER_OAUTH_TOKEN_SECRET)
    #twitter.verify_credentials()
    twitter.update_status(status=tweet.text.encode('utf-8'))
        
