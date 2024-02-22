from .models import Customer
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('pk',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your lastname'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your phone number'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your company name'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter country'
            }),
            'address_1': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter address 1'
            }),
            'address_2': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter address 2'
            }),
            'town': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter town'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'state'
            }),
        }