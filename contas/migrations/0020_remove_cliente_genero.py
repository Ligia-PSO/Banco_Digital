# Generated by Django 4.0.6 on 2022-07-18 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0019_alter_contabancaria_conta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='genero',
        ),
    ]
