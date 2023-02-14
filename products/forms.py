from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField()
    price = forms.FloatField()
    image = forms.ImageField()
    class Meta:
        model = Product
        fields = "__all__"
