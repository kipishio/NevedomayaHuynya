#-*- coding: utf-8 -*-
from django.contrib import admin
from KatalogCvetov.models import CvetiKatalog, KommentariyCvetka, ReytingCvetka, VidiRasteniy,PhotoView


# класс делает показ комментариев сразу з комментария в админке к одной каталожной
# еденицы при открытии этой еденицы
class KommentariyCvetka_Inline (admin.TabularInline):
    # указываем клас созданый в моделях
    model = KommentariyCvetka
    # указываем количество строк которое будет выводится от класса KommentariyCvetka
    extra = 3

class ReytingCvetka_Inline (admin.TabularInline):
    # указываем клас созданый в моделях
    model = ReytingCvetka
    # указываем количество строк которое будет выводится от класса KommentariyCvetka
    extra = 1

class VidiRasteniyAdmin (admin.ModelAdmin):
    fieldsets = [(None,{'fields':['name_vida',]})]

class PhotoView_Inline(admin.TabularInline):
    model = PhotoView
    fieldsets = [(None,{'fields':['photo',]})]
    extra = 2

#указываем в какой последовательности будут расположены поля и что часть
# полей будет свернута на это указывапет 'classes':['collapse'
class CvetiKatalogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['VidiRasteniy','name_rosteniya','cena','photo']}),
        ('Подробная инормация',{'fields':['opisanie','coderjat','polza','sposob_razmnogeniya','peresadka',
                                          'osobennosty_uhod','temperatera','svet','poliv','vlajnost_vozduha',
                                          'pochva','pub_date'], 'classes':['collapse']}),
    ]
# class ReytingCvetka(admin.ModelAdmin):

    # указываем что комментарии будут сокращенно кратко (KommentariyCvetka_Inline клас соданый выше) + рейтинг
    inlines = [KommentariyCvetka_Inline,ReytingCvetka_Inline,PhotoView_Inline,]

    #Указываем какие будут показываться колонки при открытии каталога со списком всех растений
    list_display = ('VidiRasteniy','name_rosteniya','cena','opisanie','pub_date')
    # Добавляет фильтр по полю нашей переменной даты в админке 'pub_date' отдельный (по дате, сегодня, последние 7 дней, этот месяц, год)
    list_filter = ['pub_date','VidiRasteniy',]
    # Добавляет поле поиска по столбцу 'name_rosteniya' в каталоге ростений в админке
    search_fields = ['name_rosteniya',]
    #количество объектов на страинице, будет выдавать по 10 наименование ростений на странице в каталоге админа
    list_per_page = 10

class KommentariyCvetkaAdmin(admin.ModelAdmin):

    fieldsets =[('Комментарий ростения',{'fields':['CvetiKatalog','kommentariy']})
    ]
    list_display = ('kommentariy','CvetiKatalog')
    list_filter = ['CvetiKatalog']
    search_fields = ['kommentariy']
    list_per_page = 10

class ReytingCvetkaAdmin(admin.ModelAdmin):
    fieldsets =[('Рейтинг ростения',{'fields':['cveti_katalog','reyting']})
    ]
    list_display = ('reyting','cveti_katalog')
    list_filter = ['cveti_katalog']
    search_fields = ['reyting']
    list_per_page = 10

# регистрируем мдели в админке чтоб они там показывались (так можно регистрировать любую модель)
#CvetiKatalogAdmin указывает что будет этот клас в котором записали в какой последовательности и как все
#будет выглядеть от класса CvetiKatalog в админке как бы указали вид интерфейса конкретно
admin.site.register(CvetiKatalog, CvetiKatalogAdmin)
admin.site.register(VidiRasteniy)
admin.site.register(ReytingCvetka, ReytingCvetkaAdmin)
admin.site.register(KommentariyCvetka, KommentariyCvetkaAdmin)
admin.site.register(PhotoView)



