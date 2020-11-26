from django import forms

from estate_app.models import AdditionalFilter, LookingFor


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


class LookingForForm(forms.ModelForm):
    class Meta:
        model = LookingFor
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }