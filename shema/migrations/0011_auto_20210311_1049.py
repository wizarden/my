# Generated by Django 3.1.7 on 2021-03-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shema', '0010_auto_20210311_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='izd',
            old_name='izd_modul',
            new_name='izd_modu2',
        ),
        migrations.RenameField(
            model_name='up',
            old_name='izd_modul',
            new_name='izd_modu2',
        ),
        migrations.RenameField(
            model_name='up',
            old_name='izd_name',
            new_name='izd_name1',
        ),
        migrations.AddField(
            model_name='izd',
            name='izd_name1',
            field=models.CharField(default='', max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='izd',
            name='izd_name',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Название полностью'),
        ),
    ]
