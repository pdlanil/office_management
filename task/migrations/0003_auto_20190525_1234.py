# Generated by Django 2.2.1 on 2019-05-25 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20190525_1014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_deadline',
            new_name='deadline',
        ),
        migrations.AlterField(
            model_name='task',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
    ]
