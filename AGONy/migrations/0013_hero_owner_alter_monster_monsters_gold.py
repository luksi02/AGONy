# Generated by Django 4.1.2 on 2022-10-11 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AGONy', '0012_alter_monster_monsters_gold_alter_origin_origin_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=6),
        ),
    ]
