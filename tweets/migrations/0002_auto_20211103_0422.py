# Generated by Django 3.2.8 on 2021-11-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'], 'verbose_name': 'Tags', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id'], 'verbose_name': 'Tweet', 'verbose_name_plural': 'Tweets'},
        ),
    ]