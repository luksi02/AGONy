# Generated by Django 4.1.2 on 2022-10-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0005_monster_monsters_gold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=9),
        ),
    ]
