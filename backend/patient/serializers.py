from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "age",
            "weight",
            "height",
            "chronic_diseases",
        )
        read_only_fields = ("id",)

