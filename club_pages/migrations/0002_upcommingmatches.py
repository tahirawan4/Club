# Generated by Django 2.0.2 on 2018-04-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpCommingMatches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField(null=True)),
                ('team1', models.CharField(max_length=250)),
                ('team2', models.CharField(max_length=250)),
                ('time', models.TimeField()),
            ],
        ),
    ]