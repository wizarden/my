# Generated by Django 3.1.7 on 2021-03-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shema', '0003_auto_20210310_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='izd',
            name='name_block',
        ),
        migrations.AddField(
            model_name='nameblock',
            name='izd',
            field=models.ManyToManyField(blank=True, to='shema.Izd', verbose_name='Изделие'),
        ),
    ]
