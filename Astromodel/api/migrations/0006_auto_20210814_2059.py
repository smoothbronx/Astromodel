# Generated by Django 3.2.6 on 2021-08-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210814_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='request',
            field=models.FileField(upload_to='jsons/1628967567.1568/'),
        ),
        migrations.AlterField(
            model_name='query',
            name='response',
            field=models.FileField(upload_to='jsons/1628967567.1568/'),
        ),
    ]
