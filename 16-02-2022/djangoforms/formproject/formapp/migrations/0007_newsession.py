# Generated by Django 4.0.2 on 2022-02-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0006_remove_student_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
