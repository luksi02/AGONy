# Generated by Django 4.1.3 on 2023-01-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0003_alter_monster_monster_ai_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=10),
        ),
    ]