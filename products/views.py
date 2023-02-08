from django.shortcuts import render
from .models import Product

# Create your views here.

def crud(request):
    items = Product.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'crud.html', context)