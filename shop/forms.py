from django import forms

class AgregarAlCarritoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1)
