from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    tel = forms.CharField()
    address = forms.Textarea()
