# Generated by Django 3.1.3 on 2020-12-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201221_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='profile_image',
            field=models.FileField(default='', upload_to='images/'),
        ),
    ]