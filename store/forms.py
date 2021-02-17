from django import forms
from .models import *


class UserEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'state', 'country', 'zipcode',)
