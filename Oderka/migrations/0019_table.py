# Generated by Django 4.0.4 on 2022-05-19 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Oderka', '0018_season_alter_club_description_match_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('loses', models.PositiveSmallIntegerField(default=0)),
                ('draws', models.PositiveSmallIntegerField(default=0)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oderka.club')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oderka.season')),
            ],
        ),
    ]
