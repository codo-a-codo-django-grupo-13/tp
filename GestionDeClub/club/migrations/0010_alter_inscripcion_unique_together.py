# Generated by Django 5.0.6 on 2024-06-12 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0009_alter_disciplina_socios'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inscripcion',
            unique_together={('socio', 'disciplina')},
        ),
    ]
