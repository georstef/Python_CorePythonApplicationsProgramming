from django.contrib import admin
from poster import models

# select which fields to show
# 'tweet' is connected to Tweet.__str__
class CommentAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'text')

# Register your models here.
admin.site.register(models.Tweet)
admin.site.register(models.Comment, CommentAdmin)
