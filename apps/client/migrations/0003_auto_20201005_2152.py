# Generated by Django 3.1.2 on 2020-10-05 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20201005_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='adress',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
