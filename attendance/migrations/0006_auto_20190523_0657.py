# Generated by Django 2.2.1 on 2019-05-23 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20190522_1911'),
    ]

    operations = [
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
