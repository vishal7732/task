# Generated by Django 3.2.8 on 2021-10-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Address_Line_1', models.CharField(max_length=500)),
                ('Address_Line_2', models.CharField(max_length=500)),
                ('City', models.CharField(max_length=100)),
                ('Phone', models.IntegerField(default=0)),
            ],
        ),
    ]
