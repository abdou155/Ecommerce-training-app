# Generated by Django 2.2.3 on 2019-07-23 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carstable',
            old_name='cylendre',
            new_name='cylindre',
        ),
    ]
