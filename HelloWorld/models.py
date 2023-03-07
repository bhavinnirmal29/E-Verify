from django.db import models
# Create your models here.
class User1(models.Model):
    firstname= models.CharField(max_length=25)
    lastname= models.CharField(max_length=25)
    date_of_birth = models.DateField()
    email= models.EmailField()
    gender= models.CharField(max_length=7)
    phonenumber= models.IntegerField()
    password = models.CharField(max_length=50)
    confirmPwd = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email

class PersonalInfo(models.Model):
    firstname= models.CharField(max_length=25)
    lastname= models.CharField(max_length=25)
    phonenumber= models.IntegerField()
    email= models.EmailField()
    occupation= models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    document_status = models.CharField(max_length=50)
    account_number = models.IntegerField()
    personal_Info_Status = models.CharField(max_length=10)