from django.db import models


# Create your models here.

class Container(models.Model):
    numLot = models.IntegerField(default=0, primary_key=True, verbose_name="Numéro du lot")
    numContainer = models.CharField(max_length=12, verbose_name="Numéro du container")
    isSQ = models.BooleanField(default=False, verbose_name="SQ")
    isC = models.BooleanField(default=False, verbose_name="Zone C")
    isF = models.BooleanField(default=False, verbose_name="Francité")
    isBloque = models.BooleanField(default=False, verbose_name="Lot bloqué")
    commentaires = models.CharField(max_length=128, blank=True, null=True, verbose_name="Commentaires")

    def __str__(self):
        return str(self.numLot) + ' - ' + str(self.numContainer)


class Score(models.Model):
    idScore = models.IntegerField(default=0, primary_key=True, verbose_name="ID du score")
    tonnage = models.CharField(max_length=12, verbose_name="Tonnage")
    depotage = models.CharField(max_length=20, verbose_name="Dépotage")
    container = models.CharField(max_length=12, verbose_name="Numéro du container")
    marque = models.CharField(max_length=8, verbose_name="Marque")
    produit = models.CharField(max_length=32, verbose_name="Produit")
    qteAnnonce = models.IntegerField(default=0, verbose_name="Qté Annoncée")
    numLot = models.IntegerField(default=0, verbose_name="Numéro du lot")
    gestion = models.CharField(max_length=128, blank=True, null=True, verbose_name="Gestion")
    prio = models.CharField(max_length=128, blank=True, null=True, verbose_name="prio")
    info = models.CharField(max_length=128, blank=True, null=True, verbose_name="info")
    resultat = models.CharField(max_length=128, blank=True, null=True, verbose_name="Résultat")
    mdc = models.CharField(max_length=128, blank=True, null=True, verbose_name="MDC")
    ncc = models.CharField(max_length=128, blank=True, null=True, verbose_name="NC/C")

    def __str__(self):
        return str(self.numLot) + ' - ' + str(self.container) + ' - ' + str(self.marque)
