from rest_framework import serializers

from . import models

 

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'body', 'username', 'user_id', 'created_at', 'comments', 'comment_count', 'likes', 'likes_count']

    def get_comment_count(self, obj):
        return models.Comment.objects.filter(post=obj).count()
    
    def get_likes_count(self, obj):
        return models.PostLike.objects.filter(post=obj).count()

 
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Comment
        fields = ['id', 'post', 'body', 'username', 'user_id', 'created_at', 'likes', 'likes_count']

    def get_likes_count(self, obj):
        return models.CommentLike.objects.filter(comment=obj).count()


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostLike
        fields = ['id']


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentLike
        fields = ['id']