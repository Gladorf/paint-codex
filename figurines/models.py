from django.db import models


class Figurine(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Step(models.Model):
    class Outil(models.TextChoices):
        PINCEAU = "pinceau", "Pinceau"
        BOMBE = "bombe", "Bombe"
        AEROGRAPHE = "aerographe", "Aérographe"
        AUTRE = "autre", "Autre"

    figurine = models.ForeignKey(
        Figurine,
        on_delete=models.CASCADE,
        related_name="steps",
    )
    description = models.TextField()
    outil = models.CharField(max_length=20, choices=Outil.choices)
    ordre = models.IntegerField()

    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return f"{self.figurine.nom} - {self.description} - {self.get_outil_display()}"