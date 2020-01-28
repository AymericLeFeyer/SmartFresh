from django.db import models

# Create your models here.

class Container(models.Model):
    numLot = models.IntegerField(default=0, primary_key=True)
    numContainer = models.CharField(max_length=16)
    isSQ = models.BooleanField(default=False)
    isC = models.BooleanField(default=False)
    isF = models.BooleanField(default=False)
    commentaires = models.CharField(max_length=128)

    def __str__(self):
        return str(self.numLot) + ' - ' + str(self.numContainer)

    

    
    
