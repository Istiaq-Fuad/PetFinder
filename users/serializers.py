
from rest_framework import serializers
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("email", "name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



# from rest_framework import serializers
# from .models import User


# class UserSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(min_length=6, write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = (
#             "id",
#             "name",
#             "email",
#             "password",
#             "is_staff",
#             "is_active",
#         )

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)

