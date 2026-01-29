from django.shortcuts import render, redirect
from inventory.models import Product
from .models import Sale, SaleItem
from django.http import JsonResponse
from inventory.models import Product


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    pid = str(product_id)

    cart[pid] = cart.get(pid, 0) + 1
    request.session['cart'] = cart

    return JsonResponse({
        "qty": cart[pid],
        "cart_count": sum(cart.values())
    })


def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    pid = str(product_id)
    action = request.POST.get('action')

    if action == "plus":
        cart[pid] = cart.get(pid, 0) + 1
    elif action == "minus":
        if cart.get(pid, 0) > 1:
            cart[pid] -= 1
        else:
            cart.pop(pid, None)

    request.session['cart'] = cart

    return JsonResponse({
        "qty": cart.get(pid, 0),
        "cart_count": sum(cart.values())
    })




def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        qty = cart.get(str(product.id), 0)
        subtotal = qty * product.price
        total += subtotal

        cart_items.append({
            'product': product,
            'qty': qty,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })



def checkout(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    total = 0
    for product in products:
        total += product.price * cart.get(str(product.id), 0)

    if request.method == "POST":
        payment_method = request.POST.get("payment")

        # ✅ create sale
        sale = Sale.objects.create(
            total_amount=total,
            payment_method=payment_method
        )

        # ✅ create sale items
        for product in products:
            qty = cart.get(str(product.id), 0)
            SaleItem.objects.create(
                sale=sale,
                product=product,
                qty=qty,
                price=product.price
            )

        # clear cart
        request.session['cart'] = {}

        # ✅ redirect WITH sale_id
        return redirect('receipt', sale_id=sale.id)

    return render(request, 'checkout.html', {'total': total})



def receipt(request, sale_id):
    sale = Sale.objects.get(id=sale_id)
    sale_items = SaleItem.objects.filter(sale=sale)

    items = []
    for item in sale_items:
        items.append({
            'product': item.product.name,
            'qty': item.qty,
            'price': item.price,
            'subtotal': item.qty * item.price
        })

    return render(request, 'receipt.html', {
        'sale': sale,
        'items': items
    })

