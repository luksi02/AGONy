# Generated by Django 4.1.2 on 2022-10-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0021_alter_monster_monsters_gold_alter_stage_monsters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=9),
        ),
        migrations.AlterField(
            model_name='stage',
            name='monsters',
            field=models.ManyToManyField(blank=True, null=True, through='AGONy.AliveMonsterInStage', to='AGONy.alivemonster'),
        ),
    ]