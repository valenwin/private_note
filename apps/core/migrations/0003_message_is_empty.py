# Generated by Django 3.1.1 on 2020-09-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200909_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_empty',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
