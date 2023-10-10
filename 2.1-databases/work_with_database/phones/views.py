from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    phone_objects = Phone.objects.all()
    phone = []
    for phones in phone_objects:
        item = {
            'name': phones.name,
            'price': phones.price,
            'image': phones.image,
            'release_date': phones.release_date,
            'lte_exists': phones.lte_exists,
            'slug': slugify(phones.name)
        }
        phone.append(item)
    if sort == 'min_price':
        context = {'phones': sorted(phone, key=lambda x: x['price'])}
    elif sort == 'max_price':
        context = {'phones': sorted(phone, key=lambda x: -x['price'])}
    else:
        context = {'phones': sorted(phone, key=lambda x: x['name'])}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    for item in phone_object:
        phone = {
            'name': item.name,
            'price': item.price,
            'image': item.image,
            'release_date': item.release_date,
            'lte_exists': item.lte_exists,
            'slug': slugify(item.name)
        }
    context = {'phone': phone}
    return render(request, template, context)
