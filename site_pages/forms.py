from django.forms import ModelForm, CharField, Form, PasswordInput
from .models import CustomerRequest, MyUser
from django import forms


class CustomerRequestForm(ModelForm):
    class Meta:
        model = CustomerRequest
        fields = ['name', 'surname', 'patronymic', 'phone' ]


class MyUserForm(ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = MyUser
        # password = forms.pas(widget=PasswordInput())
        fields = [
            'name',
            'surname',
            'patronymic',
            'phone',
            'password',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'password': forms.PasswordInput(),
        }
