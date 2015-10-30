from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = "Category"
 
    def __unicode__(self):
        return self.name
 
class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=255, blank=True, editable=False, null=True)
    category = models.ForeignKey(Category,related_name='post_category', null=True)
    # content = models.TextField(blank=True, null=True)
    content = tinymce_models.HTMLField(blank=True, null=True)
    creator = models.ForeignKey(User, related_name='user_post', default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = "Post"
 
    def __unicode__(self):
        return self.title