# Generated by Django 4.0.2 on 2022-02-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_delete_sess_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
