from django.forms import ModelForm
from django import forms
from .models import *

from django.core.validators import RegexValidator

class AddPropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'contact_us_first_name',
            'class': 'contact_us_form_group',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'contact_us_last_name',
            'class': 'contact_us_form_group',
            'placeholder': 'Last Name'
        })
    )
    phone_number = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=r'^\d{3}-\d{3}-\d{4}$',
                message="Enter a valid phone number (e.g., 444-444-4444)."
            )
        ],
        widget=forms.TextInput(attrs={
            'id': 'contact_us_phone_number',
            'class': 'contact_us_form_group',
            'placeholder': '444-444-4444'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'id': 'contact_us_email',
            'class': 'contact_us_form_group',
            'placeholder': 'Email'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'contact_us_message',
            'class': 'contact_us_form_group',
            'rows': 5,
            'placeholder': 'Message'
        }),
        required=True
    )
