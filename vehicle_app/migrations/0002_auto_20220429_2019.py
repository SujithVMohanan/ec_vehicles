# Generated by Django 3.0.1 on 2022-04-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allvehicles',
            name='v_img',
            field=models.ImageField(blank=True, upload_to='vehicle'),
        ),
    ]
