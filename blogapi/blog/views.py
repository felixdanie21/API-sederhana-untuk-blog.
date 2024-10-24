# blog/views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# ListCreateAPIView: Mengambil semua post (GET) dan membuat post baru (POST)
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# RetrieveUpdateDestroyAPIView: Mengambil post by ID (GET), mengupdate (PUT/PATCH), dan menghapus (DELETE)
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
