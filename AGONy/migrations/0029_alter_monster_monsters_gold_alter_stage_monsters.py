# Generated by Django 4.1.2 on 2022-10-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0028_remove_stagex_game_remove_stagex_monsters_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=7),
        ),
        migrations.AlterField(
            model_name='stage',
            name='monsters',
            field=models.ManyToManyField(through='AGONy.AliveMonsterInStage', to='AGONy.alivemonster'),
        ),
    ]
