# Generated by Django 3.2.6 on 2021-08-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20210816_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='request',
            field=models.FileField(upload_to='jsons/1629139318.393459/'),
        ),
        migrations.AlterField(
            model_name='query',
            name='response',
            field=models.FileField(upload_to='jsons/1629139318.393459/'),
        ),
    ]
