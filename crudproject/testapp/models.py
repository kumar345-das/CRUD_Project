from pyexpat import model
from django.db import models

# Create your models here.


#. First name, last name,gender,email.
class Student(models.Model):
    First_name=models.CharField(max_length=60)
    Last_name=models.CharField(max_length=60)
    Gender=models.CharField(max_length=1, choices=( ('M', 'Male'),('F', 'Female'),))
    Email=models.EmailField()
    

