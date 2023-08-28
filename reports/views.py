from rest_framework import generics, permissions
from .serializers import ReportSerializer
from .models import Report

class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Test perform_create and request data fro post_id
    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = Post.objects.get(pk=post_id)
        serializer.save(reporter=self.request.user, post=post)

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAdminUser]
