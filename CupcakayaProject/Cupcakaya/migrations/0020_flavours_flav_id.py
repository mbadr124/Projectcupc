# Generated by Django 4.2 on 2023-05-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0019_remove_item_flavour_item_flavour'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavours',
            name='flav_id',
            field=models.IntegerField(null=True),
        ),
    ]
