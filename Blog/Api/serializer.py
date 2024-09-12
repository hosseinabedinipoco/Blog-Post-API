from rest_framework import serializers
from .models import Post

class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'tags', 'created_at', 'update_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("title is very small")
        return value    
    
    def validate_category(self, value):
        if value not in ['Technology', 'Education', 'shopping']:
            raise serializers.ValidationError('this category is unknown')
        return value