from django.contrib import admin

from .models import *




class UpAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Up._meta.fields]
    fields = ('up_izd', 'up_num', 'up_type', ('up_color', 'up_color_group', ), )



    class Meta:
        model = Up


admin.site.register(UpType)
admin.site.register(Up, UpAdmin)


class UpInline(admin.StackedInline):  # TabularInline

    model = Up
    fields = ('up_izd', 'up_num', 'up_type', ('up_color', 'up_color_group', ), ('izd_title', 'izd_name1', 'izd_name2',),)
    extra = 1

    """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    """





class IzdAdmin (admin.ModelAdmin):

    # readonly_fields = ('izd_col',)
    list_display = ('izd_cod', 'izd_name', 'izd_col', )

    list_filter = ('izd_cod', 'izd_name', )
    search_fields = ('izd_cod', 'izd_name', )
    inlines = [UpInline, ]

    fields = (('izd_cod', 'izd_name', 'izd_col',), ('izd_title', 'izd_name1', 'izd_name2',), 'izd_des', )

    # fields = ('title',)

    save_on_top = True
    save_as = True

    # list_editable = ('izd_name', )
    """
    def save_model(self, request, obj, form, change):
        # ups_izd = Up.objects.filter(up_izd__id=obj.id)
        # ups_izd_count = ups_izd.count()
        obj.izd_col = request.POST['up_set-TOTAL_FORMS']
        print(request.POST['up_set-TOTAL_FORMS'])

        # for n in range(obj.izd_col):
        # up = Up.objects.create(up_num=n + 1, up_izd=Izd(id=obj.id))
        #    print(n)

        # for n in ups_izd:
        #    print(n)

        # ups_izd.delete() # удалить все

        return super(IzdAdmin, self).save_model(request, obj, form, change)
    """

admin.site.register(Izd, IzdAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_cod', 'color_name', 'color_type')
    search_fields = ['color_name', 'color_cod', 'color_type']
    list_display_links = ['color_name', 'color_cod', 'color_type']


#    list_display_links = [field.name for field in Color._meta.fields]
#   list_filter = ('color_cod', 'color_name')
#   list_filter = (('color_cod', admin.BooleanFieldListFilter), 'color_name')

 
admin.site.register(Color, ColorAdmin)
admin.site.register(ColorGroup)



"""
class UpAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Up._meta.fields]

    class Meta:
        model = Up

admin.site.register(UpType)
admin.site.register(Up, UpAdmin)


class UpInline(admin.TabularInline):
    model = Up
    filter_vertical = ('izd_color', 'color_group',)
    extra = 0


class IzdAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Izd._meta.fields]
    list_display_links = [field.name for field in Izd._meta.fields]
    inlines = [UpInline]
    readonly_fields = ('izd_col', )
    list_filter = ('izd_cod', 'izd_name')

    def save_model(self, request, obj, form, change):

        # ups_izd = Up.objects.filter(up_izd__id=obj.id)
        # ups_izd_count = ups_izd.count()
        obj.izd_col = request.POST['up_set-TOTAL_FORMS']
        print(request.POST['up_set-TOTAL_FORMS'])


        #for n in range(obj.izd_col):
            # up = Up.objects.create(up_num=n + 1, up_izd=Izd(id=obj.id))
        #    print(n)

        #for n in ups_izd:
        #    print(n)

        # ups_izd.delete() # удалить все

        return super(IzdAdmin, self).save_model(request, obj, form, change)

    class Meta:
        model = Izd


admin.site.register(Izd, IzdAdmin)

"""



