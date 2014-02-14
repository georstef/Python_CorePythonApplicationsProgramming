from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from site02 import settings
from poster.models import Tweet 

#create the on_the_fly autoform here not in models.py
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        # only show fields text and author_email
        fields = ('text', 'author_email')
        # text field must be memo (3rows x 50cols)
        widgets = {
            'text': forms.Textarea(attrs={'cols':50, 'rows':3}),
            }

# Create your views here.
def post_tweet(request, tweet_id=None):
    tweet = None
    if tweet_id:
        # get a tweet object/record based on the id
        tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        # this is called when the submit button is pressed
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.state = 'pending'
            new_tweet.save()
            #send_review_email()
            return HttpResponseRedirect('/post/thankyou')
    else:
        # get a filled tweet form based on a tweet object/record
        form = TweetForm(instance=tweet)
    # it shows the form if tweet is None then the form is empty else 
    # the form has default values from the selected tweet object/record 
    return render(request, 'post_tweet.html', {'form': form})

def send_review_email():
    subject = 'Action required: review tweet'
    body = ('A new tweet has been created.', 'approve or reject it.')
    #subject - body - from_email - to_emails
    # automagicaly finds username/password from the settings file
    send_mail(subject. body, settings.DEFAULT_FROM_EMAIL, [settings.TWEET_APPROVER_EMAIL])

def thank_you(request):
    # gets how many tweets are pending 
    tweets_in_queue = Tweet.objects.filter(
        state='pending').aggregate(Count('id'))['id__count']
    return render(request, 'thank_you.html', {'tweets_in_queue': tweets_in_queue})
