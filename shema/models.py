from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, verbose_name="Тег")

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Color(models.Model):
    color_cod = models.CharField(max_length=4, verbose_name="Код")
    color_name = models.CharField(max_length=100, verbose_name="Название")
    color_des = models.TextField(default="", verbose_name="Коментарий", blank=True)
    color_type = models.CharField(max_length=10, default="", verbose_name="Тип", blank=True)

    def __str__(self):
        return '(%s) %s' % (self.color_cod, self.color_name)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = ['color_cod']


class ColorGroup(models.Model):
    color_group_name = models.CharField(max_length=100, verbose_name="Название группы")
    color_list = models.ManyToManyField(Color, blank=True, verbose_name="Цвета")
    color_group_des = models.TextField(default="", verbose_name="Коментарий", blank=True)

    def __str__(self):
        return '%s' % self.color_group_name

    class Meta:
        verbose_name = 'Группа цветов'
        verbose_name_plural = 'Группа цветов'


class Izd(models.Model):
    izd_cod = models.CharField(max_length=4, default="", verbose_name="Код")
    izd_name = models.CharField(blank=True, max_length=200, default="", verbose_name="Название полностью")

    izd_title = models.CharField(max_length=100, default="", verbose_name="Заголовок")
    izd_name1 = models.CharField(max_length=100, default="", verbose_name="Имя")
    izd_name2 = models.CharField(max_length=100, default="", verbose_name="Модуль")

    izd_des = models.TextField(blank=True, default="", verbose_name="Коментарий")
    izd_col = models.IntegerField(default=1, verbose_name="Количество упаковок")
    # izd_tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")

    def __str__(self):
        return '(%s) %s' % (self.izd_cod, self.izd_name)



    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'


class UpType(models.Model):
    uptype_etik = models.CharField(max_length=20, verbose_name="Этикетка")
    uptype_des = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return self.uptype_des

    class Meta:
        verbose_name = 'Тип упаковки'
        verbose_name_plural = 'Тип упаковки'


class Up(models.Model):
    up_izd = models.ForeignKey(Izd, on_delete=models.PROTECT, default="")

    izd_title = models.CharField(max_length=100, default="", verbose_name="Заголовок")
    izd_name1 = models.CharField(max_length=100, default="", verbose_name="Имя")
    izd_name2 = models.CharField(max_length=100, default="", verbose_name="Модуль")

    up_num = models.CharField(max_length=2, verbose_name="№ упак.")
    up_type = models.ForeignKey(UpType, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Тип")
    up_color = models.ManyToManyField(Color, blank=True, verbose_name="Цвет")
    up_color_group = models.ManyToManyField(ColorGroup, blank=True, verbose_name="Группа цветов")

    def __str__(self):
        return '%s - %s' % (self.up_num, self.up_type)

    class Meta:
        verbose_name = 'Упаковка'
        verbose_name_plural = 'Упаковки'
        ordering = ['up_num', 'up_type']







