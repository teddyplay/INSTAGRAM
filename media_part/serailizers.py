from rest_framework import serializers
from users.admin import User
from media_part.models import Post
from media_part.models import Likes




class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=5,
                                     max_length=20,
                                     )


    class Meta:
        model = User
        fields = ["username",
                  ]




class PostSeializer(serializers.ModelSerializer):
    author = serializers.HiddenField(required=False,
                                     default=serializers.CurrentUserDefault(),
                                     )
    image = serializers.ImageField(

                                   )
    description = serializers.CharField(min_length=5,
                                        max_length=80,
                                        )
    hashtags = serializers.CharField(min_length=1,
                                    max_length=20,
                                    )
    likes = serializers.SerializerMethodField(
        method_name="get_count_of_likes",
    )


    class Meta:
        model = Post
        fields = ["id",
                  "author",
                  "author_id",
                  "image",
                  "description",
                  "hashtags",
                  "likes",
                  ]


    def get_count_of_likes(self, obj):
        return Likes.objects.filter(post=obj).count()





class LikesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)




    class Meta:
        model = Likes
        fields = ["author",
                  ]











