from builtins import super
from django.contrib.auth import get_user
from employee.models import Employee
from attendance.models import leave, daily_attendance
from task.models import Task
import datetime
from django import forms


class TaskForm(forms.ModelForm):
    task_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}))
    assign_time = forms.DateField(initial=datetime.date.today,
                                  widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    deadline = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    task_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}))

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['emp_id'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                       queryset=Employee.objects.all())

    class Meta:
        model = Task
        fields = ['task_name', 'emp_id', 'assign_time', 'deadline', 'task_description']


class EmployeeForm(forms.ModelForm):
    emp_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name of employee'}))
    emp_id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unique id of employee'}))
    emp_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    emp_phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
    emp_email = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'contact email'}))

    class Meta:
        model = Employee
        fields = ['emp_name', 'emp_id', 'emp_address', 'emp_phone', 'emp_email']


class AttendanceForm(forms.ModelForm):
    employee_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name of employee'}))
    attendance_date = forms.DateField(initial=datetime.date.today,
                                      widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date of attendance'}))
    entry_time = forms.TimeField(initial=datetime.datetime.now,
                                 widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'entry inside office'}))
    exit_time = forms.TimeField(initial=datetime.datetime.now,
                                widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'exit  time from office'}))

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['emp_id'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                       queryset=Employee.objects.all())

    class Meta:
        model = daily_attendance
        fields = ['employee_name', 'attendance_date', 'entry_time', 'exit_time', 'emp_id']


class LeaveForm(forms.ModelForm):
    employee_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name of employee'}))
    leave = forms.DateField(initial=datetime.datetime.now,
                            widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'Date of leave'}))

    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)
        self.fields['emp_id'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                       queryset=Employee.objects.all())

    class Meta:
        model = leave
        fields = ['employee_name', 'emp_id', 'leave']
