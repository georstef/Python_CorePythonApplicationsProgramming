from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=140)
    author_email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    STATE_CHOICES = ( # this is not a field but a const/enum
        ('pending', 'pending'),
        ('published', 'published'),
        ('rejected', 'rejected'),
        )
    state = models.CharField(max_length=15, choices=STATE_CHOICES)

    # for python 2.x
    #def __unicode__(self):
    #    return self.text

    # for python 3.x
    def __str__(self):
        return self.text

    # to add a default ordering and other stuff like permissions
    class Meta:
        permissions = (
            ('can_approve_or_reject_tweet', 'Can approve or reject tweets'),
            )

class Comment(models.Model):
    tweet = models.ForeignKey(Tweet)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

