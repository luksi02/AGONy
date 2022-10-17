# Generated by Django 4.1.2 on 2022-10-14 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0026_alter_monster_monsters_gold'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliveMonsterInStagex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.alivemonster')),
            ],
        ),
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=6),
        ),
        migrations.CreateModel(
            name='Stagex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('visited', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.hero')),
                ('monsters', models.ManyToManyField(blank=True, null=True, through='AGONy.AliveMonsterInStagex', to='AGONy.alivemonster')),
            ],
        ),
        migrations.AddField(
            model_name='alivemonsterinstagex',
            name='stagex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.stagex'),
        ),
    ]