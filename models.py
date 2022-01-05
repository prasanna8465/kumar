from django.db import models

# Create your models here.
class seller(models.Model):
    NAME=models.CharField(max_length=60)
    DESCRIPTION=models.TextField(max_length=50)
    COSTPERITEM=models.DecimalField(max_digits=7,decimal_places=3)
    STOCKQUANTITY=models.DecimalField(max_digits=7,decimal_places=3)
    VOLUME=models.DecimalField(max_digits=7,decimal_places=3,null=True,blank=True)

    def item(self):
        a=self.COSTPERITEM * self.STOCKQUANTITY
        return a

    def save(self):
        self.VOLUME=self.item()
        super(seller,self).save()

    def __str__(self):
        return self.NAME


