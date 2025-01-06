from rest_framework import serializers


from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')

    def validate_group(self, value):
        if not Group.objects.filter(pk=value):
            raise serializers.ValidationError('Такой группы не существует!')
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    text = serializers.CharField(required=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')
