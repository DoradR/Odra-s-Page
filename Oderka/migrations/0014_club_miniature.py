# Generated by Django 4.0.4 on 2022-05-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oderka', '0013_typeofdetails_alter_details_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='miniature',
            field=models.ImageField(blank=True, null=True, upload_to='Miniatures'),
        ),
    ]
