# Generated by Django 4.1.2 on 2022-10-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0017_alter_monster_monsters_gold_alter_stage_hero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=5),
        ),
    ]
