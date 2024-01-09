from django import forms
from .models import GeneralCustomization, Tools, ConfigurationSetting

class GeneralCustomizationForm(forms.ModelForm):
    class Meta:
        model = GeneralCustomization
        fields = '__all__'


class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = '__all__'
        

class ConfigurationSettingForm(forms.ModelForm):
    class Meta:
        model = ConfigurationSetting
        fields = '__all__'