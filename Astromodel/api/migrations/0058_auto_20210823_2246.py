# Generated by Django 3.2.6 on 2021-08-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_auto_20210823_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='request',
            field=models.FileField(upload_to='jsons/1629751584.677005/'),
        ),
        migrations.AlterField(
            model_name='query',
            name='response',
            field=models.FileField(upload_to='jsons/1629751584.677005/'),
        ),
    ]
