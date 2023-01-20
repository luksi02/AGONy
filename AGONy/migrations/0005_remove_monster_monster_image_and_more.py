# Generated by Django 4.1.3 on 2023-01-06 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0004_alter_monster_monsters_gold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='monster_image',
        ),
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=7),
        ),
        migrations.CreateModel(
            name='MonsterMonsterImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.monster')),
                ('monster_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.monsterimage')),
            ],
        ),
        migrations.AddField(
            model_name='monster',
            name='monster_monster_image',
            field=models.ManyToManyField(through='AGONy.MonsterMonsterImage', to='AGONy.monsterimage'),
        ),
    ]
