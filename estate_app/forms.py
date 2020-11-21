from django import forms

from estate_app.models import AdditionalFilter


class AdditionalFilterForm(forms.ModelForm):
    class Meta:
        model =AdditionalFilter
        fields = '__all__'

        widgets = {
            'sale_or_rent': forms.Select(attrs={
                'class': 'form-control'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'number_rooms': forms.Select(attrs={
                'class': 'form-control'
            }),
            'sort': forms.Select(attrs={
                'class': 'form-control'
            }),
        }