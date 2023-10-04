from rest_framework import generics, permissions, serializers
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer, ProfileReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from profiles.models import Profile  # Import the Profile model

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile_id')
        
        # Ensure that profile_id is provided in the request data
        if not profile_id:
            raise serializers.ValidationError("profile_id is required when creating a review.")
        
        # Use profile_id to fetch the associated profile
        profile = get_object_or_404(Profile, pk=profile_id)

        # Associate the review with the specified profile
        serializer.save(owner=self.request.user, profile=profile)

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return Review.objects.filter(profile_id=profile_id)
        else:
            return Review.objects.all()

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
        else:
            self.permission_denied(self.request)

    def permission_denied(self, request):
        self.raise_exception(permissions.PermissionDenied("You do not have permission to edit this review."))

class ProfileReviews(generics.ListAPIView):
    serializer_class = ProfileReviewSerializer

    def get_queryset(self):
        profile_id = self.kwargs['profile_id']
        return Review.objects.filter(profile_id=profile_id)
