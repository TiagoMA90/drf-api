from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Report
        fields = ['id', 'reporter', 'post_id', 'reason', 'created_at']
