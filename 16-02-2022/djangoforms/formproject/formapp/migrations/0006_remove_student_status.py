# Generated by Django 4.0.2 on 2022-02-12 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0005_alter_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
    ]