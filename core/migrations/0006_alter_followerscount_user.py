# Generated by Django 4.1.2 on 2022-11-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_followerscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerscount',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
