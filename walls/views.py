from rest_framework import generics
from rest_framework import permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import WallPost
from .serializers import WallPostSerializer

class WallPostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WallPostSerializer
    queryset = WallPost.objects.all()

    def perform_create(self, serializer):
        profile = self.request.user.profile  # Assuming you have a profile associated with the user
        serializer.save(author=self.request.user, profile=profile)

class WallPostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WallPostSerializer
    queryset = WallPost.objects.all()
