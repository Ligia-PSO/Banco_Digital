# Generated by Django 4.0.6 on 2022-07-10 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0008_rename_cliente_contabancaria_titular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contabancaria',
            name='conta',
            field=models.PositiveIntegerField(default=78076, editable=False, primary_key=True, serialize=False),
        ),
    ]
