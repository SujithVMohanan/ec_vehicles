# Generated by Django 3.0.1 on 2022-04-30 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0005_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]