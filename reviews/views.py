from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


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

    def get_object(self):
        review_id = self.kwargs['pk']
        review = get_object_or_404(Review, pk=review_id)
        return review

    def perform_update(self, serializer):
        review = self.get_object()

        if self.request.user == review.owner:
            serializer.save()
            return Response(serializer.data)
        else:
            raise PermissionDenied("You do not have permission to edit this review.")