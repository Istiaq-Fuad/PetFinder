from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "id",
            "pet",
            "user",
            "status",
            "pet_experience",
            "house_condition",
        ]
        read_only_fields = ["user", "status"]

    def validate(self, data):
        user = self.context["request"].user
        validated_data = super(ApplicationSerializer, self).validate(data)
        if Application.objects.filter(**validated_data, user=user).exists():
            raise serializers.ValidationError("this application already exists")
        return data


class ApplicationPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "id",
            "pet",
            "user",
            "status",
            "pet_experience",
            "house_condition",
        ]
        read_only_fields = ["id", "user", "pet"]
