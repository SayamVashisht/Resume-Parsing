# Generated by Django 2.1.4 on 2019-03-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0009_resume_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='competencies',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Skills'),
        ),
    ]