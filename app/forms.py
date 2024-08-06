from django.forms import ModelForm
from django.forms import forms
from .models import *

class AddPropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'