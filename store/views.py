import json

from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Subcategory, Product
from django.core.paginator import Paginator
from .forms import ReviewForm


# Create your views here.
def get_subcategory(request):
    _id = request.GET.get('id', '')
    result = list(Subcategory.objects.filter(category_id=int(_id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def home_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/index.html', context)


def shop_view(request):
    query = request.GET.get('sort')

    if not query:
        products = Product.objects.filter(quantity__gt=0)
        print([x.quantity for x in products])
    else:
        products = Product.objects.filter(quantity__gt=0).order_by(query)

    # 30, 3
    # {1: [obj1, obj2, obj3]}
    # {2: [obj4, obj5, obj6]}
    # {3: [obj1, obj2, obj3]}
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products
    }
    return render(request, 'store/shop.html', context)


def subcategory_products(request, slug):
    ''''''
    # получить объект подкатегории по ее slug
    # получить все продукты полученной подкатегории
    # отдать полученные элементы на страницу shop
    # создать url для данной функции со значением в name='subcategory_products'
    query = request.GET.get('sort')

    subcategory = Subcategory.objects.get(slug=slug)

    if not query:
        products = Product.objects.filter(subcategory=subcategory, quantity__gt=0)
    else:
        products = Product.objects.filter(subcategory=subcategory, quantity__gt=0).order_by(query)

    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products
    }
    return render(request, 'store/shop.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)

    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.author = request.user
            form.save()
            return redirect('store:detail', product.slug)
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'form': form,
        'reviews': reviews
    }
    return render(request, 'store/detail.html', context)
