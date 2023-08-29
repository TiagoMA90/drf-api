from rest_framework import serializers
from .models import WallPost

class WallPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = WallPost
        fields = ['id', 'author', 'profile', 'content', 'created_at']
