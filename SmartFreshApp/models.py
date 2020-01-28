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

    

    
    
