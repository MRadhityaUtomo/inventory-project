# Generated by Django 4.2.5 on 2023-09-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item_attack_item_defense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='attack',
            field=models.IntegerField(default='0000000', editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='defense',
            field=models.IntegerField(default='0000000', editable=False),
        ),
    ]