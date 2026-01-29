from inventory.models import Product, Category
from django.shortcuts import render

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})