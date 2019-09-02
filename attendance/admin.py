from django.contrib import admin
from attendance.models import daily_attendance
from attendance.models import leave

# Register your models here.
admin.site.register(daily_attendance)
admin.site.register(leave)
