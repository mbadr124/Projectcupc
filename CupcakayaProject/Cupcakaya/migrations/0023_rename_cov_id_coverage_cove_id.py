# Generated by Django 4.2 on 2023-05-17 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0022_remove_item_amount_remove_item_coverage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coverage',
            old_name='cov_id',
            new_name='cove_id',
        ),
    ]
