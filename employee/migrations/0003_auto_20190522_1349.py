# Generated by Django 2.2.1 on 2019-05-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190522_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
