from django.contrib import admin
from blog import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    
# Register your models here.
admin.site.register(models.BlogPost, BlogPostAdmin)
