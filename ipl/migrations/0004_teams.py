# Generated by Django 2.2.1 on 2019-06-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0003_matches_match_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
    ]
