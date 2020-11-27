from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_name', 'product_image','product_isAvailable','product_quantity')

        def __str__(self):
            return self.product_name