# Create your views here.
from django.shortcuts import render, redirect
from .forms import GeneralCustomizationForm, ToolsForm
from .models import GeneralCustomization, Tools
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
    # You'll create home.html later in your templates


def home_assistant(request):
    return render(request, 'home_assistant.html')


def tools(request):
    try:
        settings = Tools.objects.first()
    except Tools.DoesNotExist:
        settings = None

    if request.method == 'POST':
        form = ToolsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved successfully') 
            return redirect('tools')
    else:
        form = ToolsForm(instance=settings)

    return render(request, 'tools.html', {'form': form, 'settings': settings})


def configuration_settings(request):
    try:
        tool_settings = Tools.objects.first()  # Retrieve the first Tools settings from the database
    except Tools.DoesNotExist:
        tool_settings = None
    return render(request, 'configuration_settings.html', {'tool_settings': tool_settings})


def general_customization(request):
    try:
        settings = GeneralCustomization.objects.first()
    except GeneralCustomization.DoesNotExist:
        settings = None

    if request.method == 'POST':
        form = GeneralCustomizationForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved successfully.')
            return redirect('general_customization')
        else:
            messages.error(request, 'Changes not saved, please fill in all the fields.')
    else:
        form = GeneralCustomizationForm(instance=settings)
    return render(request, 'general_customization.html', {'form': form, 'settings': settings})