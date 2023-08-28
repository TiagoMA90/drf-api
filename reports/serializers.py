from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')
    post = serializers.StringRelatedField()

    class Meta:
        model = Report
        fields = [
            'id',
            'reporter',
            'post',
            'post_id',
            'reason',
            'created_at',
        ]
