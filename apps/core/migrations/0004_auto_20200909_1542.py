# Generated by Django 3.1.1 on 2020-09-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_message_is_empty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]