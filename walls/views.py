from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Wall
from .serializers import WallSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class WallList(generics.ListCreateAPIView):
    serializer_class = WallSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Wall.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WallDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WallSerializer

    def get_object(self):
        wall_id = self.kwargs['pk']
        wall = get_object_or_404(Wall, pk=wall_id)
        return wall

    def perform_update(self, serializer):
        wall = self.get_object()
        if self.request.user == wall.owner:
            serializer.save()
        else:
            self.permission_denied(self.request)

    def permission_denied(self, request):
        self.raise_exception(permissions.PermissionDenied("You do not have permission to edit this Wall post."))

class ProfileWalls(generics.ListAPIView):
    serializer_class = WallSerializer

    def get_queryset(self):
        profile_id = self.kwargs['profile_id']
        return Wall.objects.filter(profile_id=profile_id)
