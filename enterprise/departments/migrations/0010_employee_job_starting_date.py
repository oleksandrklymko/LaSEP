# Generated by Django 3.1.3 on 2020-12-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0009_employee_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_starting_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
