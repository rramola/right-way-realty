from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class AddPropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = "__all__"


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "id": "contact_us_first_name",
                "class": "contact_us_form_group",
                "placeholder": "First Name",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "id": "contact_us_last_name",
                "class": "contact_us_form_group",
                "placeholder": "Last Name",
            }
        ),
    )
    phone_number = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=r"^\d{3}-\d{3}-\d{4}$",
                message="Enter a valid phone number (e.g., 123-456-7890).",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "id": "contact_us_phone_number",
                "class": "contact_us_form_group",
                "placeholder": "123-456-7890",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "id": "contact_us_email",
                "class": "contact_us_form_group",
                "placeholder": "Email",
            }
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "id": "contact_us_message",
                "class": "contact_us_form_group",
                "rows": 5,
                "placeholder": "Message",
            }
        ),
        required=True,
    )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    # username = form.CharField(
    #     max_length=15,
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "id": "username-container",
    #             "class": "form_group",
    #             "placeholder": "Username",
    #         }
    #     ),
    # )
    # first_name = forms.CharField(
    #     max_length=30,
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "id": "first-name-container",
    #             "class": "form_group",
    #             "placeholder": "First Name",
    #         }
    #     ),
    # )
    # last_name = forms.CharField(
    #     max_length=30,
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "id": "last-name-container",
    #             "class": "form_group",
    #             "placeholder": "Last Name",
    #         }
    #     ),
    # )
    # phone_number = forms.CharField(
    #     required=True,
    #     validators=[
    #         RegexValidator(
    #             regex=r"^\d{3}-\d{3}-\d{4}$",
    #             message="Enter a valid phone number (e.g., 123-456-7890).",
    #         )
    #     ],
    #     widget=forms.TextInput(
    #         attrs={
    #             "id": "phone-number-container",
    #             "class": "form_group",
    #             "placeholder": "123-456-7890",
    #         }
    #     ),
    # )
    # email = forms.EmailField(
    #     required=True,
    #     widget=forms.EmailInput(
    #         attrs={
    #             "id": "email-container",
    #             "class": "form_group",
    #             "placeholder": "Email",
    #         }
    #     ),
    # )
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2']
