from django import forms
from .models import Model1, Model2, Model3

class Model1Form(forms.ModelForm):
    class Meta:
        model = Model1
        fields = ['field1', 'field2']

class Model2Form(forms.ModelForm):
    class Meta:
        model = Model2
        fields = ['field1', 'field2']

class Model3Form(forms.ModelForm):
    class Meta:
        model = Model3
        fields = ['field1', 'field2']
