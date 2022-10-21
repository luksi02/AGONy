# Generated by Django 4.1.2 on 2022-10-21 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AliveMonster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_hp', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AliveMonsterInStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.alivemonster')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentEventInJourney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.currentevent')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_type', models.IntegerField(choices=[(0, 'Monster Encounter'), (1, 'Loot Encounter'), (2, 'Trap Encounter'), (3, 'Empty Encounter')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('race', models.IntegerField(choices=[(0, 'Human'), (1, 'Elf'), (2, 'Dwarf')], default=0)),
                ('hp', models.IntegerField(default=100)),
                ('attack', models.IntegerField(default=5)),
                ('defence', models.IntegerField(default=0)),
                ('backstory', models.TextField(blank=True, default='')),
                ('gold', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hp', models.IntegerField(default=20)),
                ('attack', models.IntegerField(default=2)),
                ('defence', models.IntegerField(default=2)),
                ('monster_level', models.IntegerField(choices=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], default=0)),
                ('monster_type', models.IntegerField(choices=[(0, 'Human'), (1, 'Wildlife'), (2, 'Undead')], default=0)),
                ('description', models.TextField(blank=True)),
                ('monsters_gold', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_type', models.IntegerField(choices=[(0, 'General'), (1, 'TragicOrigin'), (2, 'Racial')], default=0)),
                ('origin_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('visited', models.BooleanField(default=False)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.hero')),
                ('monsters', models.ManyToManyField(through='AGONy.AliveMonsterInStage', to='AGONy.alivemonster')),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('day_visited', models.BooleanField(default=False)),
                ('event', models.ManyToManyField(through='AGONy.CurrentEventInJourney', to='AGONy.currentevent')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.hero')),
                ('next_day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev', to='AGONy.journey')),
            ],
        ),
        migrations.AddField(
            model_name='currenteventinjourney',
            name='journey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.journey'),
        ),
        migrations.AddField(
            model_name='currentevent',
            name='current_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.event'),
        ),
        migrations.AddField(
            model_name='alivemonsterinstage',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.stage'),
        ),
        migrations.AddField(
            model_name='alivemonster',
            name='monster_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.monster'),
        ),
    ]
