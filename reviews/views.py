from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer, ProfileReviewSerializer
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
        print(f"Review ID: {review.id}")
        print(f"Request User: {self.request.user}")

        if self.request.user == review.owner:
            serializer.save()
            return Response(serializer.data)
        else:
            print("Permission Denied: User is not the owner.")
            raise PermissionDenied("You do not have permission to edit this review.")

class ProfileReviews(generics.ListAPIView):
    serializer_class = ProfileReviewSerializer

    def get_queryset(self):
        profile_id = self.kwargs['profile_id']
        return Review.objects.filter(profile_id=profile_id)