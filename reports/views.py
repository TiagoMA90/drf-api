from rest_framework import generics, permissions
from .serializers import ReportSerializer
from .models import Report

from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ReportSerializer
from .models import Report

class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        reason = self.request.data.get('reason')
        
        if not post_id or not reason:
            raise serializers.ValidationError('Both post and reason are required.')
        
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise serializers.ValidationError('Post not found.')
        
        serializer.save(reporter=self.request.user, post=post, reason=reason)


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAdminUser]
