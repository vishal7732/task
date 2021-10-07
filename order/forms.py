from django.core import validators
from django import forms
from .models import Address
from .models import Orders

class SaveAddress(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['user', 'First_Name', 'Last_Name','Address_Line_1','Address_Line_2','City','Phone']

