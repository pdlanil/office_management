# Generated by Django 2.2.1 on 2019-05-28 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20190525_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
    ]