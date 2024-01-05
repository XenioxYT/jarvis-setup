from django import forms
from .models import GeneralCustomization, Tools

class GeneralCustomizationForm(forms.ModelForm):
    class Meta:
        model = GeneralCustomization
        fields = '__all__'


class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = '__all__'