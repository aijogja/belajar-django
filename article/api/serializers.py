from rest_framework import serializers
from article.models import Category, Post

# Create your views here.


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_on', 'last_modified')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'category', 'content', 'creator', 'status', 'created_on', 'last_modified')

class PostChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'category', 'content', 'creator', 'status')
