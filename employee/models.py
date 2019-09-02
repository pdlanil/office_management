from django.db import models
from django.db import models
from datetime import *
from django.utils import timezone


class Employee(models.Model):
    emp_name=models.CharField(max_length=200,null=False,blank=False)
    emp_id=models.IntegerField(null=False,blank=False,primary_key=True,unique=True)
    emp_address=models.CharField(max_length=200)
    emp_phone=models.IntegerField(blank=False)
    emp_email=models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.emp_name
