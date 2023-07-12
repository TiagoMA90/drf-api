from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'The Image is too big!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'The Image is too wide, please upload it with a width below 4096px!!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'The Image is too long, please upload it with a height below 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'is_owner',
            'profile_id',
            'profile_image',
        ]