# Generated by Django 2.2.5 on 2019-10-25 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terra_accounts', '0007_terrapermission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='terrauser',
            options={'ordering': ['id']},
        ),
    ]
