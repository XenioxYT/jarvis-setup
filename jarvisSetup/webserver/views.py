# Create your views here.
from django.shortcuts import render, redirect
from .forms import GeneralCustomizationForm, ToolsForm, ConfigurationSettingForm
from .models import GeneralCustomization, Tools, ConfigurationSetting, SetupFlow
from dotenv import load_dotenv, dotenv_values, set_key
from django.contrib import messages
from pathlib import Path

def home(request):
    Tools.objects.get_or_create(id=1)
    GeneralCustomization.objects.get_or_create(id=1)
    ConfigurationSetting.objects.get_or_create(id=1)
    SetupFlow.objects.get_or_create(id=1)
    setup_flow = SetupFlow.objects.first()
    setup_flow.save()
    return render(request, 'home.html', {'setup_flow': setup_flow})


def home_assistant(request):
    return render(request, 'home_assistant.html')


def tools(request):
    Tools.objects.get_or_create(id=1)
    GeneralCustomization.objects.get_or_create(id=1)
    ConfigurationSetting.objects.get_or_create(id=1)
    try:
        settings = Tools.objects.first()
    except Tools.DoesNotExist:
        settings = None

    if request.method == 'POST':
        form = ToolsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Changes saved successfully') 
            # change the setup flow to the next step, "tools"
            setup_flow = SetupFlow.objects.first()
            print(setup_flow.setup_flow)
            setup_flow.setup_flow = "config"
            setup_flow.save()
            return redirect('home')
    else:
        form = ToolsForm(instance=settings)

    return render(request, 'tools.html', {'form': form, 'settings': settings})


def configuration_settings(request):
    Tools.objects.get_or_create(id=1)
    GeneralCustomization.objects.get_or_create(id=1)
    ConfigurationSetting.objects.get_or_create(id=1)
    tool_settings = Tools.objects.first()

    if request.method == 'POST':
        # Manually extract the values from the POST data
        keys = [
            'picovoice_access_key', 'openai_api_key', 'openai_api_base', 'discord_token',
            'google_api_key', 'google_cse_id', 'google_maps_api_key', 'home_assistant_token',
            'home_assistant_url'
        ]

        # Fetch or create a single ConfigurationSetting instance
        config, _ = ConfigurationSetting.objects.get_or_create(id=1)

        variables = {}

        for key in keys:
            value = request.POST.get(key)
            if value not in ['None', None, '']:
                setattr(config, key, value)
                variables[key] = value

        config.save()

        with open('.env', 'w') as file:
            for var, value in variables.items():
                if value not in ['None', None]:
                    file.write(f'{var}={value}\n')

        # Save the changes
        try:
            config.save()
        except Exception as e:
            messages.error(request, f'Error saving configuration: {e}')
            return redirect('configuration_settings')

        # messages.success(request, 'Configuration updated successfully!')
        setup_flow = SetupFlow.objects.first()
        setup_flow.setup_flow = "done"
        setup_flow.save()
        return redirect('home')
    
    # If GET request, prepare the context
    try:
        current_config = ConfigurationSetting.objects.get(id=1)
    except ConfigurationSetting.DoesNotExist:
        current_config = None
    context = {
        'tool_settings': tool_settings,
        'current_config': current_config,
    }
    return render(request, 'configuration_settings.html', context)


def general_customization(request):
    Tools.objects.get_or_create(id=1)
    GeneralCustomization.objects.get_or_create(id=1)
    ConfigurationSetting.objects.get_or_create(id=1)
    try:
        settings = GeneralCustomization.objects.first()
    except GeneralCustomization.DoesNotExist:
        settings = None

    if request.method == 'POST':
        form = GeneralCustomizationForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Changes saved successfully.')
            setup_flow = SetupFlow.objects.first()
            setup_flow.setup_flow = "tools"
            setup_flow.save()
            return redirect('home')
        else:
            messages.error(request, 'Changes not saved, please fill in all the fields.')
    else:
        form = GeneralCustomizationForm(instance=settings)
    return render(request, 'general_customization.html', {'form': form, 'settings': settings})