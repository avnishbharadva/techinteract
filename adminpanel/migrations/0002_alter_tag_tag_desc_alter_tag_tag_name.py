# Generated by Django 4.1.5 on 2024-03-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_desc',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=20),
        ),
    ]
