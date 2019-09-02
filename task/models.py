from django.db import models
from datetime import *
from employee.models import Employee

# Create your models here.

class Task(models.Model):
    task_name=models.CharField(max_length=200,null=False)
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    assign_time=models.DateField(default=datetime.now)
    deadline=models.DateField()
    task_description=models.TextField(max_length=500)


    def __str__(self):
        return self.task_name

