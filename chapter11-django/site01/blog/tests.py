# this module does not work correctly.....something is wrong

from datetime import datetime
from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from blog.models import BlogPost
class BlogPostTest(TestCase):
    def test_obj_create(self):
        BlogPost.objects.create(title='raw title', body='raw body', timestamp=datetime.now())
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('raw title', BlogPost.objects.get(id=1).title)

    def test_home(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_slash(self):
        response = self.client.get('/')
        #30x is for redirection but we haven't made a redirection
        #at least not in urls.py but only in views.py
        self.assertIn(response.status_code, (301, 302))

    def test_empty_create(self):
        response = self.client.get('/blog/create/')
        #30x is for redirection but we haven't made a redirection
        #at least not in urls.py but only in views.py
        self.assertIn(response.status_code, (301, 302))

    def test_post_create(self):
        response = self.client.post('/blog/create/',
                                    {'title': 'post title','body': 'post body'})
        self.assertIn(response.status_code, (301, 302))
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('post title', BlogPost.objects.get(id=1).title)
