from django import forms

class ProductForm(forms.Form):
    address = forms.URLField(widget=forms.TextInput(
        attrs={'placeholder': 'آدرس محصول مورد نظرت از دیجیکالا', 
        'type': 'url'}
        ))
    wage = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'حقوق ماهیانه به ریال', 
        'type': 'number'}
        ))