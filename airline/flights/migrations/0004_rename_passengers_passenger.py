# Generated by Django 3.2.7 on 2021-09-05 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passengers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passengers',
            new_name='Passenger',
        ),
    ]
