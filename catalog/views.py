from django.shortcuts import render
from products.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def catalog_all(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by("-id")
    
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'catalog/catalog.html', locals())


def kruzhevo(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3)
    main_category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    # new_items = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__new_items=True)
    # hit_items = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__hit_items=True)

    return render(request, 'catalog/catalog.html', locals())


def elastichnoe(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=15)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=15)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    return render(request, 'catalog/catalog.html', locals())

def na_setke(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=1)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=1)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    return render(request, 'catalog/catalog.html', locals())

def s_resnichkami(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=2)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=2)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'catalog/catalog.html', locals())


def polotno(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=3)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=3)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'catalog/catalog.html', locals())


def shantili(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=4)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=3, product__subcategories=4)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'catalog/catalog.html', locals())

def elastichnaja_tesma(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4)
    main_category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def breteli(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4, product__subcategories=5)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4, product__subcategories=5)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def kosaja_bejka(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4, product__subcategories=6)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4, product__subcategories=6)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def tonnelnaja_lenta(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4, product__subcategories=7)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4, product__subcategories=7)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def believye_rezinki(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4, product__subcategories=8)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=4, product__subcategories=8)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def furnitura(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5)
    main_category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def krjuchki(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5, product__subcategories=9)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5, product__subcategories=9)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def zastezhki(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5, product__subcategories=10)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5, product__subcategories=10)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def kostochki(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5, product__subcategories=11)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5, product__subcategories=11)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'catalog/catalog.html', locals())

def believoj_paralon(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5, product__subcategories=12)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=5, product__subcategories=12)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def prochee(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=6)
    main_category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=6)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())

def dekorativnye_elementy(request):
    products_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=6, product__subcategories=13)
    category = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=6, product__subcategories=13)[:1]
    paginator = Paginator(products_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request, 'catalog/catalog.html', locals())