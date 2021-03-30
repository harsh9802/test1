from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class complaint_table(models.Model):
    AadharNumber=models.IntegerField()
    cdesc=models.CharField(max_length=50)
    City=models.CharField(max_length=15)

class Dl_table(models.Model):
    AadharNumber=models.IntegerField()
    Name=models.CharField(max_length=25)
    cov=models.CharField(max_length=10)
    email_id=models.EmailField()
    City=models.CharField(max_length=15)
    dl_id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.AadharNumber + self.Name + self.City

class llr_table(models.Model):
    llr_id=models.AutoField(primary_key=True)
    AadharNumber=models.IntegerField()
    Name=models.CharField(max_length=25)
    password=models.CharField(max_length=15,unique=True)
    email_id=models.EmailField()
    dateofbirth=models.DateField()
    City=models.CharField(max_length=15)
    Address=models.CharField(max_length=200)
    Gender=models.CharField(max_length=6)
    VehicleType=models.CharField(max_length=7)

    def __str__(self):
        return self.city + self.password + self.llr_id


class registration_table(models.Model):
    r_id=models.AutoField(primary_key=True)
    aadharNumber=models.IntegerField()
    name=models.CharField(max_length=25)
    cov=models.CharField(max_length=15)
    password=models.CharField(max_length=25,unique=True)
    model=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    reg_issue_date=models.DateField()
    reg_expiry_date=models.DateField()
    mail_id=models.EmailField()
    Gender=models.CharField(max_length=8)
    fuel_type=models.CharField(max_length=9)
    vehicle_category=models.CharField(max_length=7)

    def __str__(self):
        return self.name + self.city
