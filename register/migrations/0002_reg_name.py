# Generated by Django 3.2.13 on 2022-06-21 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='name',
            field=models.CharField(default='not available', max_length=50),
        ),
    ]
