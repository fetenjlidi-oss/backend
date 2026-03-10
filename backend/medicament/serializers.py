from rest_framework import serializers

from .models import Medicament


class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = (
            "id",
            "name",
            "dosage_ref",
            "description",
        )
        read_only_fields = ("id",)