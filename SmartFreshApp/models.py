from django.db import models

# Create your models here.

class Container(models.Model):
    numLot = models.IntegerField(default=0)
    numContainer = models.CharField(max_length=16)
    isSQ = models.BooleanField(default=0)
    isC = models.BooleanField(default=0)
    isF = models.BooleanField(default=0)
    commentaires = models.CharField(max_length=128)

    def __str__(self):
        return str(self.numLot) + ' - ' + str(self.numContainer)

    
    
