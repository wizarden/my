# Generated by Django 3.1.7 on 2021-03-10 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shema', '0006_auto_20210310_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nameblock',
            old_name='izd_name1',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='nameblock',
            old_name='izd_name2',
            new_name='name2',
        ),
        migrations.RenameField(
            model_name='nameblock',
            old_name='izd_title',
            new_name='title',
        ),
    ]
