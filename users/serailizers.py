from rest_framework import serializers
from .models import User



class RegisUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(min_length=4,
                                     max_length=10,

                                     )
    password = serializers.CharField(min_length=5,
                                     max_length=10,
                                     )
    phone = serializers.IntegerField(min_value=13,
                                     max_value=15
                                     )



    class Meta:
        model = User
        fields = ["email",
                  "username",
                  "password",
                  "phone",
                  ]




    def validate(self, attrs):
        email_exists = User.objects.filter(email = attrs[
            "email"
        ]).exists()
        if email_exists:
            raise ValueError("Такая электронная почта уже используется!")
        return super().validate(attrs)



    def create(self, validated_data):
        password = validated_data.pop(
            "password",
        )
        user = super().create(validated_data)


        user.set_password(
            password,
        )


        user.save()
        return user



class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=10,
                                   max_length=20,
                                   )
    username = serializers.CharField(min_length=4,
                                     max_length=10
                                     )
    phone = serializers.IntegerField(min_value=13,
                                     max_value=15,
                                     )



    class Meta:
        model = User
        fields = ["email",
                  "username",
                  "phone",
                  ]
