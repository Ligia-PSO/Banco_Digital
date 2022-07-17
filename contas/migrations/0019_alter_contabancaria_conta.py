# Generated by Django 4.0.6 on 2022-07-17 17:57

import contas.models.contabancaria
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0018_alter_contabancaria_conta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contabancaria',
            name='conta',
            field=models.PositiveIntegerField(default=contas.models.contabancaria.ContaBancaria.conta_num_aleatorio, editable=False, primary_key=True, serialize=False),
        ),
    ]
