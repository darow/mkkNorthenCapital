from django.forms import ModelForm
from .models import Customer_request


class Customer_form(ModelForm):
    class Meta:
        model = Customer_request
        fields = ['name', 'surname', 'patronymic', 'phone']