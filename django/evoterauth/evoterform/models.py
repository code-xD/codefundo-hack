from django.db import models

# Create your models here.


class CacheVoterData(models.Model):
    voter_name = models.CharField(max_length=200)
    gender = models.IntegerField()
    age = models.IntegerField()
    s_code = models.IntegerField()
    c_code = models.IntegerField()
    d_code = models.IntegerField()
    pin = models.IntegerField()
    aLine1 = models.CharField(max_length=500)
    aLine2 = models.CharField(max_length=500)
    aadhar_no = models.BigIntegerField()
    voter_photo = models.ImageField()
    aadhar_card = models.ImageField()
    address_proof = models.ImageField()

    def __str__(self):
        return self.voter_name+'-'+str(self.aadhar_no)
