# Generated by Django 2.1.4 on 2018-12-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0005_auto_20181229_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile Number'),
        ),
        
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Education'),
        )
    ]
