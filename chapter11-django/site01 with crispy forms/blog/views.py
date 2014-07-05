"""
# try if view.py works
from django.shortcuts import render
from datetime import datetime
from blog.models import BlogPost

# Create your views here.
def archive(request):
    post = BlogPost(title='mocktitle', body='mockbody', timestamp=datetime.now())
    return render(request, 'archive.html', {'posts': [post]})
"""

'''
# formal way of view functions
from django.http import HttpResponse
from django.template import loader, Context
from blog.models import BlogPost

def archive(request):
    # Query the database for all blog entries
    posts = BlogPost.objects.all()

    # Load the template file
    t = loader.get_template('archive.html')

    # Create the context dictionary for the template (template params)
    c = Context({'posts': posts})

    # Pass the context to the template
    # Render the template into HTML
    # Return the HTML via the HTTP response
    return HttpResponse(t.render(c))
'''

# new short way of view functions
from django.shortcuts import render, render_to_response
from blog.models import BlogPost, BlogPostForm

from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # pagination


def archive(request):
    # get the data from the table
    # posts = BlogPost.objects.all() # query the database for all blog entries
    # posts = BlogPost.objects.all().order_by('-timestamp') # descending timestamp
    # posts = BlogPost.objects.all().order_by('-timestamp')[:3] # only 3 per page
    # posts = BlogPost.objects.all()[:3] # default ordering in models.BlogPost class

    # for pagination
    posts_list = BlogPost.objects.all()
    paginator = Paginator(posts_list, 3)  # Show 3 blogposts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    
    # use "render" over "render_to_response" (not sure why but do it)
    # update: in "render_to_response" we must add RequestContext(request) for CSRF protection
    # eg. render_to_response('archive.html', {'posts': posts,}, RequestContext(request))
    # in "render" we don't have to do this (that's why we always use "render")
    return render(request, 'archive.html', {'posts': posts, 'form': BlogPostForm()})


def base_template(request):
    posts = BlogPost.objects.all()[:3]  # default ordering in models.BlogPost class
    return render(request, 'index.html', {'posts': posts})


'''
# normal form action
def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(title=request.POST.get('title'),
                 body=request.POST.get('body'),
                 timestamp=datetime.now(),
                 ).save()

    # redirect to parent page
    return HttpResponseRedirect('/blog/')
'''


# model form action
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # this returns a BlogPost object
            #uncomment next line if timestamp has default value
            #post.timestamp = datetime.now()
            post.save()

    # redirect to parent page
    return HttpResponseRedirect('/blog/')
