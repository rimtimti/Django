# Generated by Django 4.2.5 on 2023-10-07 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_rename_client_id_order_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='goods_id',
            new_name='goods',
        ),
    ]
