# Generated by Django 3.2.6 on 2021-08-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20210823_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='request',
            field=models.FileField(upload_to='jsons/1629749654.16577/'),
        ),
        migrations.AlterField(
            model_name='query',
            name='response',
            field=models.FileField(upload_to='jsons/1629749654.16577/'),
        ),
    ]
