from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response #TEST
from rest_framework import status #TEST


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()

    def perform_update(self, serializer): #TEST
        if self.request.user == serializer.instance.owner: #TEST
            serializer.save() #TEST
            return Response(serializer.data) #TEST
        else: #TEST
            return Response( #TEST
                {"detail": "You do not have permission to edit this review."}, #TEST
                status=status.HTTP_403_FORBIDDEN #TEST
            ) #TEST