from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer
from django.views.generic import TemplateView

class ReactAppView(TemplateView):
    template_name = "index.html"



class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


