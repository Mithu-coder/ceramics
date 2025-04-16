from django.db import models

# Create your models here.

class fac_challan(models.Model):
    itemcode=models.CharField(max_length=22)
    item_des=models.CharField(max_length=44)
    qty=models.PositiveIntegerField()
    image=models.ImageField(upload_to='images/',null=True,blank=True)
