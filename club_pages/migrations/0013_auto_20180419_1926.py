# Generated by Django 2.0 on 2018-04-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0012_auto_20180419_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dynamicdata',
            name='footer_col_1',
        ),
        migrations.AddField(
            model_name='dynamicdata',
            name='footer_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='dynamicdata',
            name='footer_email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='dynamicdata',
            name='footer_no',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
