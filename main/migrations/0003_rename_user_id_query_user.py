# Generated by Django 4.1.5 on 2024-02-28 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_query'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='user_id',
            new_name='user',
        ),
    ]
