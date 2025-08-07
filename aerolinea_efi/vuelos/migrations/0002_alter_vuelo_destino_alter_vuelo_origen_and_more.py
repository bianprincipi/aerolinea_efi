from django.db import migrations, models
from datetime import timedelta

class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_remove_boleto_codigo_remove_boleto_emitido_and_more'),
        ('vuelos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelo',
            name='destino',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='origen',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='AsientoClase',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='tripulacion',
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='duracion',
            field=models.DurationField(default=timedelta(0)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='estado',
            field=models.CharField(choices=[('Programado', 'Programado'), ('En vuelo', 'En vuelo'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='fecha_llegada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='fecha_salida',
            field=models.DateTimeField(),
        ),
        migrations.DeleteModel(
            name='Aeropuerto',
        ),
        migrations.DeleteModel(
            name='Tripulante',
        ),
    ]
