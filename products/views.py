from django.shortcuts import render, redirect
from .models import Product
from . forms import ProductForm

# Create your views here.

def crud(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.POST.get('image')
        product = Product(
            name = name,
            price = price,
            image = image,
        )
        product.save()
        return redirect('crud')
        
    items = Product.objects.all()
    context = {
        'items': items,
        'form': ProductForm,
    }
    return render(request, 'crud.html', context)
