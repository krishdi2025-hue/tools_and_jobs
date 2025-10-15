from django.db import models


# Create your models here.
class Signup(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    job_field = models.CharField(max_length=35)
    updated_on = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.email

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=30)
    email1 = models.CharField(max_length=30)
    msg = models.CharField(max_length=1000)
    updated_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        return  self.full_name


