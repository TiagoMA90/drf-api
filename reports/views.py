from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from .models import Report
from .serializers import ReportSerializer

class ReportCreate(generics.CreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(reporter=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
