# Generated by Django 2.2.1 on 2019-05-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_id', models.IntegerField(max_length=5)),
                ('emp_address', models.CharField(max_length=200)),
                ('emp_phone', models.IntegerField(max_length=12)),
                ('emp_email', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
