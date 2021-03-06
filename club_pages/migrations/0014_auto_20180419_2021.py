# Generated by Django 2.0 on 2018-04-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0013_auto_20180419_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dynamicdata',
            name='footer_address',
        ),
        migrations.RemoveField(
            model_name='dynamicdata',
            name='footer_col_2',
        ),
        migrations.RemoveField(
            model_name='dynamicdata',
            name='footer_col_3',
        ),
        migrations.RemoveField(
            model_name='dynamicdata',
            name='footer_email',
        ),
        migrations.RemoveField(
            model_name='dynamicdata',
            name='footer_no',
        ),
        migrations.AlterField(
            model_name='dynamicdata',
            name='page_data',
            field=models.CharField(choices=[('home', 'Home'), ('about', 'About'), ('footer1', 'Footer1'), ('footer2', 'Footer2')], default='home', max_length=250),
        ),
    ]
