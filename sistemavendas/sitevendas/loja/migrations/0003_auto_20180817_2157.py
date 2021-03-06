# Generated by Django 2.1 on 2018-08-17 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20180817_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Perfil'),
        ),
    ]
