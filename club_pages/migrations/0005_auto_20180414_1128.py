# Generated by Django 2.0 on 2018-04-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0004_fixture_match_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixture',
            name='match_date',
        ),
        migrations.AlterField(
            model_name='fixture',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]