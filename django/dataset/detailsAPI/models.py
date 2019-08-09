from django.db import models

# Create your models here.


class VoterDetail(models.Model):
    voter_name = models.CharField(max_length=200)
    gender = models.IntegerField()
    age = models.IntegerField()
    s_code = models.IntegerField()
    c_code = models.IntegerField()
    d_code = models.IntegerField()
    pin = models.IntegerField()
    aLine1 = models.CharField(max_length=500)
    aLine2 = models.CharField(max_length=500)
    aadhar_no = models.BigIntegerField(primary_key=True, unique=True)

    def __str__(self):
        return self.voter_name+'-'+str(self.aadhar_no)
