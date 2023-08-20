from rest_framework import generics
from rest_framework import permissions
from reports.models import Report
from reports.serializers import ReportSerializer
from posts.models import Post
from drf_api.permissions import IsOwnerOrReadOnly

class ReportCreate(generics.CreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(pk=post_id)
        serializer.save(user=self.request.user, post=post)

class ReportList(generics.ListAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Report.objects.filter(post_id=post_id)

class ReportDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Report.objects.filter(post_id=post_id)
