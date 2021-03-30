# Generated by Django 3.1.7 on 2021-03-10 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='UpType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uptype_etik', models.CharField(max_length=20, verbose_name='Этикетка')),
                ('uptype_des', models.CharField(max_length=100, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тип упаковки',
                'verbose_name_plural': 'Тип упаковки',
            },
        ),
        migrations.AlterModelOptions(
            name='up',
            options={'ordering': ['up_num', 'up_type'], 'verbose_name': 'Упаковка', 'verbose_name_plural': 'Упаковки'},
        ),
        migrations.RemoveField(
            model_name='izd',
            name='izd_html',
        ),
        migrations.RemoveField(
            model_name='izd',
            name='izd_name1',
        ),
        migrations.RemoveField(
            model_name='izd',
            name='izd_name2',
        ),
        migrations.RemoveField(
            model_name='izd',
            name='izd_title',
        ),
        migrations.RemoveField(
            model_name='izd',
            name='izd_up',
        ),
        migrations.AddField(
            model_name='up',
            name='up_color',
            field=models.ManyToManyField(blank=True, to='shema.Color', verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='up',
            name='up_izd',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='shema.izd'),
        ),
        migrations.AlterField(
            model_name='up',
            name='up_num',
            field=models.CharField(max_length=2, verbose_name='№ упак.'),
        ),
        migrations.CreateModel(
            name='ColorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_group_name', models.CharField(max_length=100, verbose_name='Название группы')),
                ('color_group_des', models.TextField(blank=True, default='', verbose_name='Коментарий')),
                ('color_list', models.ManyToManyField(blank=True, to='shema.Color', verbose_name='Цвета')),
            ],
            options={
                'verbose_name': 'Группа цветов',
                'verbose_name_plural': 'Группа цветов',
            },
        ),
        migrations.AddField(
            model_name='up',
            name='up_color_group',
            field=models.ManyToManyField(blank=True, to='shema.ColorGroup', verbose_name='Группа цветов'),
        ),
        migrations.AddField(
            model_name='up',
            name='up_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shema.uptype', verbose_name='Тип'),
        ),
    ]