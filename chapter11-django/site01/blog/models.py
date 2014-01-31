from django.db import models
from django import forms

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    # to add a default ordering 
    class Meta:
        ordering = ('-timestamp',)

#for django-model-form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('timestamp',) # remove this field from the form
    
'''
#for django-forms
from django import forms
# stand-alone Form object
class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':60})
    timestamp = forms.DateTimeField()

'''
