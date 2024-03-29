# Generated by Django 2.2.1 on 2019-05-24 07:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20190523_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_attendance',
            name='attendance_date',
            field=models.DateField(default=datetime.date.today, verbose_name='date published:'),
        ),
        migrations.AlterField(
            model_name='daily_attendance',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
    ]
