# Generated by Django 2.1 on 2018-08-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_auto_20180818_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status_order',
            field=models.CharField(choices=[('P.R', 'Pedido Realizado'), ('P.R', 'Pedido Realizado'), ('S.E', 'Separação em Estoque'), ('MTG', 'Em montagem'), ('R.T', 'Realização de testes')], default='P.R', max_length=3),
        ),
    ]
