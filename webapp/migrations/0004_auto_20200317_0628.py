# Generated by Django 2.2.1 on 2020-03-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200317_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='host',
            field=models.CharField(default='localhost', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='password',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='port',
            field=models.IntegerField(default=3306),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='username',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]
