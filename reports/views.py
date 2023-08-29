from rest_framework import generics
from rest_framework import permissions
from drf_api.permissions import IsOwnerOrReadOnly
from reports.models import Report
from reports.serializers import ReportSerializer
from posts.models import Post

class ReportList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReportDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
