from django.db import models

# Create your models here.
class profile(models.Model):
    GENDER = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other')

    ]

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=2,choices=GENDER)
    address = models.TextField()
    password = models.CharField(max_length=10)
    conf_password = models.CharField(max_length=10)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Userdetails(models.Model):
    u_name = models.CharField(max_length=50,null=True,blank=True)
    u_address = models.TextField(null=True,blank=True)
    u_birthdate = models.DateField(null=True,blank=True)





