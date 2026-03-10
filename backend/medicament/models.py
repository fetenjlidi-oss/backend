from django.db import models

class Medicament(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    dosage_ref = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "Medicament"
# Create your models here.
