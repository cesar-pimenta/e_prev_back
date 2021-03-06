# Generated by Django 3.1.2 on 2020-10-06 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20201006_0017'),
        ('store', '0004_auto_20201005_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Itens'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.profile'),
        ),
    ]
