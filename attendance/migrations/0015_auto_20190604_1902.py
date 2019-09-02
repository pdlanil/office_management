# Generated by Django 2.2.1 on 2019-06-04 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0014_auto_20190604_1856'),
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
