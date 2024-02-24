from typing import Any
from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    """
    Форма сохранения нового продукта
    """
    name = forms.CharField(min_length=3,max_length=100,widget=forms.TextInput)
    image = forms.FileField(required=True,widget=forms.FileInput)
    price = forms.CharField(min_length=3,max_length=100,widget=forms.TextInput)
    quantity  = forms.CharField(min_length=1,max_length=10)
    description = forms.Textarea()

     
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        image = cleaned_data.get("image")
        description = cleaned_data.get("description")
        price = cleaned_data.get("price")
        quantity = cleaned_data.get("quantity")
        if name  and description and price and quantity and image:
            return cleaned_data
        raise forms.ValidationError("Неверное заполение формы")
    
    class Meta:
        model= Product
        fields= ["name","description","price", "image","quantity"]
   