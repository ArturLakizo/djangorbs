# Generated by Django 2.1.2 on 2018-10-20 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='some_text',
        ),
    ]
