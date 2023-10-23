from django import forms
from .models import Country


class CurrencyForm(forms.Form):
    currency1 = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        label="Select base currency"
    )
