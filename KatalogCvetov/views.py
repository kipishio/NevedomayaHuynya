# -*- coding: utf-8 -*-
from itertools import combinations
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from setuptools.command.sdist import re_finder
from KatalogCvetov.models import CvetiKatalog, ReytingCvetka, KommentariyCvetka, VidiRasteniy
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def test(request):
    KatalogCvetov = CvetiKatalog.objects.all()
    VidiRasteniySpisok = VidiRasteniy.objects.all()
    context = {'KatalogCvetov': KatalogCvetov, 'VidiRasteniySpisok': VidiRasteniySpisok}
    return render(request, 'katalogcvetov/test.html', context)


# def index(request):
#     latest_katalogcvetov = CvetiKatalog.objects.order_by('pub_date')[:5]
#     output = ', '.join([p.name_rosteniya for p in latest_katalogcvetov])
#     return HttpResponse('Последние 5-ть забитых ростений в каталог: %s.' % output)

def index(request):
    context = {'': ''}
    return render(request, 'katalogcvetov/index.html', context)


def katalog(request):

    page = request.GET.get('page',False)


    if (request.GET.get('sortvid', False)) and (request.GET.get('sortrost', False)) :
        sortvid = request.GET['sortvid']
        sortrost = request.GET['sortrost']
        page = request.GET.get('page',False)

        if (request.GET.get('vid', False)):

            if (sortvid == 'vidsortza') and (sortrost == 'rostensortza'):
                CvetiKatalog_list = CvetiKatalog.objects.all().order_by("-VidiRasteniy__name_vida", "name_rosteniya")
                sortvid = 'vidsortaz'
                sortrost = 'rostensortza'
                tekstvid = 'я-А'
                tekstrost ='А-я'


            elif (sortvid == 'vidsortaz') and (sortrost == 'rostensortaz'):
                CvetiKatalog_list = CvetiKatalog.objects.all().order_by("VidiRasteniy__name_vida", "-name_rosteniya")
                sortvid = 'vidsortza'
                sortrost = 'rostensortaz'
                tekstvid = 'А-я'
                tekstrost ='я-А'

            elif (sortvid == 'vidsortaz') and (sortrost == 'rostensortza'):
                CvetiKatalog_list = CvetiKatalog.objects.all().order_by("VidiRasteniy__name_vida", "name_rosteniya")
                print('test')
                sortvid = 'vidsortza'
                sortrost = 'rostensortza'
                tekstvid = 'А-я'
                tekstrost ='А-я'

            elif (sortvid == 'vidsortza') and (sortrost == 'rostensortaz'):
                CvetiKatalog_list = CvetiKatalog.objects.all().order_by("-VidiRasteniy__name_vida", "-name_rosteniya")
                print('test')
                sortvid = 'vidsortaz'
                sortrost = 'rostensortaz'
                tekstvid = 'я-А'
                tekstrost ='я-А'


        if (request.GET.get('rost', False)):

            if (sortvid == 'vidsortza') and (sortrost == 'rostensortza'):
                CvetiKatalog_list = CvetiKatalog.objects.all().order_by("VidiRasteniy__name_vida", "-name_rosteniya")

                sortvid = 'vidsortza'
                sortrost = 'rostensortaz'
                tekstvid = 'А-я'
                tekstrost = 'я-А'


            elif (sortvid == 'vidsortaz') and (sortrost == 'rostensortaz'):
                CvetiKatalog_list = CvetiKatalog.objects.all().order_by("-VidiRasteniy__name_vida", "name_rosteniya")
                sortvid = 'vidsortaz'
                sortrost = 'rostensortza'
                tekstvid = 'я-А'
                tekstrost = 'А-я'

            elif (sortvid == 'vidsortaz') and (sortrost == 'rostensortza'):
                CvetiKatalog_list = CvetiKatalog.objects.all().order_by("-VidiRasteniy__name_vida", "-name_rosteniya")

                sortvid = 'vidsortaz'
                sortrost = 'rostensortaz'
                tekstvid = 'я-А'
                tekstrost = 'я-А'

            elif (sortvid == 'vidsortza') and (sortrost == 'rostensortaz'):
                CvetiKatalog_list = CvetiKatalog.objects.all().order_by("VidiRasteniy__name_vida", "name_rosteniya")
                sortvid = 'vidsortza'
                sortrost = 'rostensortza'
                tekstvid = 'А-я'
                tekstrost = 'А-я'

    else:
        # KatalogCvetov = CvetiKatalog.objects.all().order_by("VidiRasteniy__name_vida", "name_rosteniya")
        CvetiKatalog_list = CvetiKatalog.objects.all().order_by("VidiRasteniy__name_vida", "name_rosteniya")
        sortvid = 'vidsortza'
        sortrost = 'rostensortza'
        tekstvid = 'А-я'
        tekstrost ='А-я'
        print('test3')
    print(CvetiKatalog_list[0].coderjat)

    paginator = Paginator(CvetiKatalog_list, 2) # показывать 25 растений на странице

    page = request.GET.get('page')
    try:
        KatalogCvetov = paginator.page(page)
    except PageNotAnInteger:
        # если страница не целое число то вызывается первая страница
        KatalogCvetov = paginator.page(1)
        page = 1
    except EmptyPage:
        # Если указанной страницы нет то открывается последняя страница
        KatalogCvetov = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    VidiRasteniySpisok = VidiRasteniy.objects.all().order_by("name_vida")
    context = locals()
    # print(context['vidsort'],789)
    # context = {'KatalogCvetov': KatalogCvetov, 'VidiRasteniySpisok': VidiRasteniySpisok, 'sortinvert': sortinvert}
    return render(request, 'katalogcvetov/katalog.html', context)


def vidrasteniya(request, id_vid_rost):
    vid = VidiRasteniy.objects.get(id=id_vid_rost)
    # проверяем если есть переменая то идем дальше по условиям, ее переменной нет то заменяес сс на False
    # и идем в else
    if request.GET.get('sort', False):
        sortget = request.GET['sort']
        if sortget == 'za':
            sortinvert = ''
            KatalogCvetov = CvetiKatalog.objects.filter(VidiRasteniy=vid).order_by("-name_rosteniya")

        elif sortget == '':
            sortinvert = 'za'
            KatalogCvetov = CvetiKatalog.objects.filter(VidiRasteniy=vid).order_by("name_rosteniya")

    else:
        sortinvert = 'za'
        KatalogCvetov = CvetiKatalog.objects.filter(VidiRasteniy=vid).order_by("name_rosteniya")


    VidiRasteniySpisok = VidiRasteniy.objects.all().order_by("name_vida")
    id_vida = id_vid_rost
    # штука ниже  собирает все в локальные переменные
    context = locals()
    # context = {'KatalogCvetov':KatalogCvetov,'VidiRasteniySpisok':VidiRasteniySpisok,'id_vida':id_vida,'sortinvert':sortinvert}
    return render(request, 'katalogcvetov/vidrasteniya.html', context)


def katalog_rastenie(request, id_rast):
    Rastenie = CvetiKatalog.objects.get(id=id_rast)
    VidiRasteniySpisok = VidiRasteniy.objects.all().order_by("name_vida")
    RasteniePhoto = Rastenie.photos.all()
    context = {'Rastenie': Rastenie, 'VidiRasteniySpisok': VidiRasteniySpisok, 'RasteniePhoto': RasteniePhoto}
    return render(request, 'katalogcvetov/rastenie.html', context)


def kontakti(request):
    context = {'': ''}
    return render(request, 'katalogcvetov/kontakti.html', context)


def onas(request):
    context = {'': ''}
    return render(request, 'katalogcvetov/onas.html', context)


# Сложная функця  запроса  ниже убдет приведена аналогичная но проще
# def ssilkirosteniy(request):
#     latest_katalogcvetov = CvetiKatalog.objects.order_by('pub_date')[:5]
#     templates = loader.get_template('katalogcvetov/index.html')
#     context = RequestContext(request,{'latest_katalogcvetov':latest_katalogcvetov,})
#     return HttpResponse(templates.render(context))
def ssilkirosteniy(request):
    latest_katalogcvetov = CvetiKatalog.objects.order_by('pub_date')[:5]
    context = {'latest_katalogcvetov': latest_katalogcvetov}
    return render(request, 'katalogcvetov/index.html', context)


def detail(request, katalogcvet_id):
    # try:
    #     cvetikatalog = CvetiKatalog.objects.get(pk = katalogcvet_id)
    # except CvetiKatalog.DoesNotExist:
    #     raise Http404 ('Нет такого ростения')
    # аналогичный код только короче ниже
    cvetikatalog = get_object_or_404(CvetiKatalog, pk=katalogcvet_id)
    for koom in cvetikatalog.kommentariycvetka_set.all():
        print(koom.kommentariy)
    return render(request, 'katalogcvetov/detail.html', {'cvetikatalog': cvetikatalog})


def results(request, cvetok_id, reyting_id, kommentari_id):
    cvetok = get_object_or_404(CvetiKatalog, pk=cvetok_id)
    reyting = get_object_or_404(ReytingCvetka, pk=reyting_id)
    kommentari = get_object_or_404(KommentariyCvetka, pk=kommentari_id)
    context = {'cvetok': cvetok, 'reyting': reyting, 'kommentari': kommentari}
    return render(request, 'katalogcvetov/result.html', context)


def vote(request, cvetikatalog_id):
    cvetok = get_object_or_404(CvetiKatalog, pk=cvetikatalog_id)

    try:
        selected_kommentari = cvetok.kommentariycvetka_set.get(pk=request.POST['kommenti'])
        selected_reyting = cvetok.reytingcvetka_set.get(pk=request.POST['reyting'])
    except (KeyError, CvetiKatalog.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'katalogcvetov/detail.html', {
            'rostenie': cvetok,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_reyting.reyting += 25
        selected_reyting.save()


        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(
        reverse('KatalogCvetov:results', args=(cvetok.id, selected_reyting.id, selected_kommentari.id,)))



    # Create your views here.
    # print( KatalogCvetovPoVidu)
