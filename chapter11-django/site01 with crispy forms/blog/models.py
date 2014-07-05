from django.db import models
from django import forms
from datetime import datetime


'''
MODELS
'''


# Create your models/tables here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())  # default is creation time

    # to add a default ordering 
    class Meta:
        ordering = ('-timestamp',)


'''
FORMS
'''


# for django-model-form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        widgets = {
            'body': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }
        exclude = ('timestamp',)  # remove this field from the form


'''

# stand-alone Form object
class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':60})
    timestamp = forms.DateTimeField()

'''
