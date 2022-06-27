# Generated by Django 4.0.5 on 2022-06-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_tenniscourt_short_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenniscourt',
            old_name='adress',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='tenniscourt',
            name='short_description',
            field=models.CharField(default='', max_length=1024),
        ),
    ]