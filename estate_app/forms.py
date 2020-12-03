from django import forms

from estate_app.models import AdditionalFilter, LookingFor, Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ('created_by', 'approved', 'counter_seen')

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'cols': 20
            }),
            'sale_or_rent': forms.Select(attrs={
                'class': 'form-control'
            }),
            'district': forms.Select(attrs={
                'class': 'form-control'
            }),
            'city': forms.Select(attrs={
                'class': 'form-control'
            }),
            'area': forms.Select(attrs={
                'class': 'form-control'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'floor': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'total_floors': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'number_rooms': forms.Select(attrs={
                'class': 'form-control'
            }),
            'furniture': forms.Select(attrs={
                'class': 'form-control'
            }),
            'elevator': forms.Select(attrs={
                'class': 'form-control'
            }),
            'built_date': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'construction': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date_modified': forms.DateInput(attrs={
                'class': 'form-control'
            }),
        }


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