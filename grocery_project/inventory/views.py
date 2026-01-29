from django.shortcuts import render, redirect

# Create your views here.

from .models import Product, Category

def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['quantity']
        Product.objects.create(name=name, price=price, quantity=qty)
        return redirect('product_list')
    return render(request, 'add_product.html')

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    q = request.GET.get('q')
    if q:
        products = products.filter(name__icontains=q)

    cat = request.GET.get('cat')
    if cat:
        products = products.filter(category_id=cat)

    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'query': q
    })
