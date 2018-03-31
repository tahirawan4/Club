# Generated by Django 2.0.2 on 2018-03-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0004_sliderimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Some String', max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='average',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='catches',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_matches',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topcategory',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club_pages.Player'),
        ),
    ]