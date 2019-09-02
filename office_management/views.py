from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime
from .forms import EmployeeForm,AttendanceForm,LeaveForm,TaskForm



def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'signup.html', context)
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("you are registered")
            form.save()
        return render(request, 'signin.html', {'form': form})


def signin(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm()

        }
        return render(request, 'signin.html', context)
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def my_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def employee(request):
    if request.method == 'GET':
        context = {
            'form': EmployeeForm(),
        }
        return render(request, 'employee.html', context)
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            mydata = form.save(commit=False)
            mydata.user_id = request.user.id
            mydata.save()
            return redirect('employee')
        return render(request, 'employee.html', {'form': form})


@login_required(login_url='login')
def task(request):
    if request.method == 'GET':
        context = {
            'form': TaskForm(),
        }
        return render(request, 'task.html', context)
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            mydata = form.save(commit=False)
            mydata.user_id = request.user.id
            mydata.save()
            return redirect('task')
        return render(request, 'task.html', {'form': form})


#ATTENDANCE
@login_required(login_url='login')
def attendance(request):
    if request.method == 'GET':
        context = {
            'form': AttendanceForm(),
        }
        return render(request, 'attendance.html', context)
    else:
        form = AttendanceForm(request.POST)
        if form.is_valid():
            mydata = form.save(commit=False)
            mydata.user_id = request.user.id
            mydata.save()
            return redirect('attendance')
        return render(request, 'attendance.html', {'form': form})

#Leave
@login_required(login_url='login')
def leave(request):
    if request.method == 'GET':
        context = {
            'form': LeaveForm(),
        }
        return render(request, 'leave.html', context)
    else:
        form = LeaveForm(request.POST)
        if form.is_valid():
            mydata = form.save(commit=False)
            mydata.user_id = request.user.id
            mydata.save()
            return redirect('leave')
        return render(request, 'leave.html', {'form': form})





