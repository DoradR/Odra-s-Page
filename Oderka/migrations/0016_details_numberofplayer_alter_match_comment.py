# Generated by Django 4.0.4 on 2022-05-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oderka', '0015_alter_player_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='numberOfPlayer',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='comment',
            field=models.TextField(max_length=516),
        ),
    ]
