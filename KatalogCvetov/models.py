#-*- coding: utf-8 -*-
from django.db import models
import datetime

# Создаем модели
class VidiRasteniy(models.Model):
    def __str__(self):
        return self.name_vida
    name_vida = models.CharField('Вид растения', max_length=200)
    class Meta(object):
        verbose_name = "Вид растения"
        verbose_name_plural = "Вид растения"


class CvetiKatalog(models.Model):
    """Клас модели цветка характеристики"""
    def __str__(self):
        return self.name_rosteniya
    #Переименовываем класс CvetiKatalog на русские названия
    class Meta(object):
        verbose_name = "Каталог цветов"
        verbose_name_plural = "Каталог цветов"
    #Переименовываем с латинского названия с помощью verbose_name="Виды растений"
    VidiRasteniy = models.ForeignKey(VidiRasteniy, verbose_name="Виды растений",related_name = 'cveti')
    name_rosteniya = models.CharField('Название цветка',max_length=200)
    cena = models.IntegerField('Цена',default=0,blank=True)
    opisanie = models.TextField('Описание',blank=True)
    coderjat = models.TextField('Содержание ростения',blank=True)
    polza = models.CharField('Польза ростения', max_length= 400,blank=True)
    sposob_razmnogeniya = models.CharField('Способ размножения',max_length=200,blank=True)
    peresadka = models.CharField('Пересадка',max_length=200,blank=True)
    osobennosty_uhod = models.CharField('Особенности ухода', max_length=200,blank=True)
    temperatera = models.CharField('Температура', max_length=200,blank=True)
    svet = models.CharField('Свет',max_length=200,blank=True)
    poliv = models.CharField('Полив', max_length=200,blank=True)
    vlajnost_vozduha = models.CharField('Влажность воздуха', max_length=200,blank=True)
    pochva = models.CharField('Почва', max_length=200,blank=True)
    pub_date = models.DateTimeField('Дата публикации',blank=True, default= datetime.datetime.now() )
    photo = models.ImageField(upload_to='preview/cveti',blank=True)


class PhotoView(models.Model):
    CvetiKatalog = models.ForeignKey(CvetiKatalog, verbose_name='Каталог цветов',related_name = 'photos')
    photo = models.ImageField('Фото',upload_to='preview/cveti',blank=True)
    # name_photo_view = models.CharField('Название фото',max_length=200)
    class Meta(object):
        verbose_name = "Фото растения"
        verbose_name_plural = "Фото растений"

class KommentariyCvetka(models.Model):
    #для нормального отображения имени класса в каталоге будет возвращать не KommentariyCvetka а сам комментарий
    def __str__(self):
        return self.kommentariy
    class Meta(object):
        verbose_name = "Комметарий"
        verbose_name_plural = "Комметарии"
    #end
    """
    Клас модели комментариев к цветку
    """
    CvetiKatalog = models.ForeignKey(CvetiKatalog, verbose_name='Каталог цветов')
    kommentariy = models.CharField('Комментарий ростения',max_length=200)

class ReytingCvetka(models.Model):
    def __str__(self):
         return ('Рейтинг растения: %s ' % self.reyting)
    class Meta(object):
        verbose_name = "Рейтинг растения"
        verbose_name_plural = "Рейтинги растиний"

    """
    Клас параметра "рейтиг" цветка интеджер
    """
    cveti_katalog = models.ForeignKey(CvetiKatalog, verbose_name= 'Каталог цветов')
    reyting = models.IntegerField('Рейтинг',default=0)









