import rest_framework.serializers as serializers
from .models import Patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'
        