# Generated by Django 5.0.6 on 2024-06-11 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_socio_fecha_alta_inscripcion_disciplina_socios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='socios',
            field=models.ManyToManyField(related_name='disciplinas', through='club.Inscripcion', to='club.socio'),
        ),
    ]