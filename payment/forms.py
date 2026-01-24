from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['user']
        widgets = {
            field: forms.TextInput(attrs={'class':'form-control', 'placeholder': field.replace("_"," ").title()})
            for field in fields if field != 'user'
        }


class PaymentForm(forms.Form):
    card_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    card_exp_date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    card_cvv_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    card_address1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    card_city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    card_country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
