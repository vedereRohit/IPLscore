# Generated by Django 2.2.1 on 2019-06-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0002_auto_20190617_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='match_id',
            field=models.IntegerField(default=-1),
        ),
    ]
