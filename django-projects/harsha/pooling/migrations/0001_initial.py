# Generated by Django 4.0.2 on 2022-03-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('option1', models.CharField(max_length=50)),
                ('option2', models.CharField(max_length=50)),
                ('option3', models.CharField(max_length=50)),
                ('option4', models.CharField(max_length=50)),
                ('v1', models.IntegerField(default=0)),
                ('v2', models.IntegerField(default=0)),
                ('v3', models.IntegerField(default=0)),
                ('v4', models.IntegerField(default=0)),
            ],
        ),
    ]
