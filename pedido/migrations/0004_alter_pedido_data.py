# Generated by Django 4.2.6 on 2023-10-19 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pedido", "0003_pedido_cupom_alter_pedido_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pedido",
            name="data",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 19, 23, 4, 39, 960293)
            ),
        ),
    ]
