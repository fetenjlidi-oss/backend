from rest_framework import serializers

from .models import Traitement


class TraitementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traitement
        fields = (
            "id",
            "dateDebut",
            "dateFin",
            "frequence",
            "instructionRepas",
        )
        read_only_fields = ("id",)