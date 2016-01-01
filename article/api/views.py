from rest_framework import generics, pagination
from rest_framework.response import Response
from article.models import Category, Post
from .serializers import CategorySerializer, PostSerializer, PostChangeSerializer

# Create your views here.

class BaseMixin(object):
    
    def get_serializer_class(self):
        if self.request.method == 'GET' and hasattr(self, 'read_serializer_class'):
            return self.read_serializer_class
        if self.request.method in ['POST', 'PUT', 'PATCH'] and hasattr(self, 'write_serializer_class'):
            return self.write_serializer_class
        return self.serializer_class

class CustomPagination(pagination.PageNumberPagination):
    page_size = None
    page_size_query_param = 'page_size'




class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(BaseMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    read_serializer_class = PostSerializer
    write_serializer_class = PostChangeSerializer
