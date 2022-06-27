# Generated by Django 4.0.5 on 2022-06-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_rename_adress_tenniscourt_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservations',
            old_name='object',
            new_name='court_object',
        ),
        migrations.AlterField(
            model_name='tenniscourt',
            name='city',
            field=models.CharField(choices=[('Białystok', 'Białystok'), ('Gdańsk', 'Gdańsk'), ('Kraków', 'Kraków'), ('Lublin', 'Lublin'), ('Olsztyn', 'Olsztyn'), ('Poznań', 'Poznań'), ('Warszawa', 'Warszawa'), ('Wrocław', 'Wrocław')], max_length=24),
        ),
    ]
