# Generated by Django 3.1.5 on 2021-01-27 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0007_auto_20210127_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='quantidade_cores',
            new_name='numero_nucleos',
        ),
    ]
