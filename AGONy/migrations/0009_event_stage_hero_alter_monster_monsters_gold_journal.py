# Generated by Django 4.1.2 on 2022-10-10 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0008_alivemonster_alivemonsterinstage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(0, 'Monster Encounter'), (1, 'Loot Encounter'), (2, 'Trap Encounter')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='stage',
            name='hero',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='AGONy.hero'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=7),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_description', models.TextField(blank=True)),
                ('alive', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGONy.event')),
            ],
        ),
    ]
