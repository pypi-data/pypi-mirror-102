# Generated by Django 2.0.9 on 2018-11-20 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terra_accounts', '0003_auto_20181023_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='readmodel',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='terrauser',
            options={'ordering': ['id'], 'permissions': (('can_manage_users', 'Is able create, delete, update users'),)},
        ),
    ]
