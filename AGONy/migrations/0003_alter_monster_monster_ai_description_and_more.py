# Generated by Django 4.1.3 on 2023-01-05 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0002_alter_monster_monster_ai_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monster_AI_description',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AGONy.monsteraidescription'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='monster_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AGONy.monsterimage'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='monsters_gold',
            field=models.IntegerField(default=5),
        ),
    ]
