# Generated by Django 4.1.5 on 2023-04-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_logteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='reffun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dis', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
