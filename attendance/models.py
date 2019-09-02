from django.db import models
from django.db import models
from datetime import *
from django.utils import timezone
from  employee.models import Employee
from django.contrib.auth.models import User


class daily_attendance(models.Model):
    employee_name = models.CharField(max_length = 500)
    attendance_date = models.DateField('date published:', default=date.today)
    entry_time=models.TimeField('entered time :',default=timezone.now)
    exit_time=models.TimeField('exit time:')
    emp_id= models.ForeignKey(Employee,on_delete=models.CASCADE)


    def __str__(self):
        return self.employee_name

class leave(models.Model):
    employee_name=models.CharField(max_length=100)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave=models.DateField(default=date.today)

    def __str__(self):
        return self.employee_name

