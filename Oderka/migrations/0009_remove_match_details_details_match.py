# Generated by Django 4.0.4 on 2022-04-19 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Oderka', '0008_match_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='details',
        ),
        migrations.AddField(
            model_name='details',
            name='match',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Oderka.match'),
            preserve_default=False,
        ),
    ]