# Generated by Django 3.0.1 on 2022-05-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='sdff', upload_to='userprofile'),
            preserve_default=False,
        ),
    ]