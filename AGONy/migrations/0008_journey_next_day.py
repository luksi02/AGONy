# Generated by Django 4.1.2 on 2022-10-17 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AGONy', '0007_rename_name_event_event_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='next_day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev', to='AGONy.journey'),
        ),
    ]