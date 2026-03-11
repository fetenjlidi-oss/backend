from django.db import models
class Rappel(models.Model):
    heure = models.DateTimeField(null=True, blank=True)
    heurePrevue = models.DateTimeField(null=True, blank=True)
    estConfirme= models.BooleanField(default=False)
    delaiSnooze = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Rappel for {self.medicament.name} at {self.time}"
# Create your models here.
