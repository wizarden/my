# Generated by Django 3.1.7 on 2021-03-11 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shema', '0007_auto_20210310_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='izd',
            name='izd_name_block',
        ),
    ]
