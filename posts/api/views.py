from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
class PostApiViewset(ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    serializer_class=PostSerializer
    queryset=Post.objects.filter(published=True)
    lookup_field='slug'
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['category__slug']
