# Generated by Django 5.2.4 on 2025-07-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
