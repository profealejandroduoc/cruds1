# Generated by Django 5.0.6 on 2024-05-31 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_mascota_subtipo_alter_mascota_edad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto',
            field=models.ImageField(null=True, upload_to='personas'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='subtipo',
            field=models.CharField(choices=[('Gato', [('Volador', 'Volador'), ('Nian', 'Nian')]), ('Otro', 'Otro'), ('PERRO', [('Chico', 'Chico'), ('Grande', 'Grande'), ('Verde', 'Verde')]), ('Reptil', [('Lagarto', 'Lagarto'), ('Anaconda', 'Anaconda')])], default='Otro', max_length=20),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.CharField(choices=[('OTRO', 'Otro'), ('GATO', 'Gato'), ('REPTIL', 'Reptil'), ('PERRO', 'Perro')], max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('O', 'OTRO'), ('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1),
        ),
    ]