from django.db import models

# Create your models here.
class GeneralCustomization(models.Model):
    assistant_name = models.CharField(max_length=100)
    wake_word = models.CharField(max_length=50)
    system_prompt = models.CharField(max_length=100)
    llm_model = models.CharField(max_length=50)
    voice_diarization = models.CharField(max_length=50)
    
class Tools(models.Model):
    live_weather = models.BooleanField(default=False)
    bbc_news = models.BooleanField(default=False)
    google_search = models.BooleanField(default=False)
    google_calendar_check = models.BooleanField(default=False)
    google_calendar_add = models.BooleanField(default=False)
    google_maps_directions = models.BooleanField(default=False)
    google_maps_info = models.BooleanField(default=False)
    set_reminder = models.BooleanField(default=False)
    list_reminder = models.BooleanField(default=False)
    edit_reminder = models.BooleanField(default=False)
    smart_home_control = models.BooleanField(default=False)
    discord_message = models.BooleanField(default=False)
    save_notes = models.BooleanField(default=False)
    list_notes = models.BooleanField(default=False)
    edit_notes = models.BooleanField(default=False)
    

class ConfigurationSetting(models.Model):
    picovoice_access_key = models.CharField(max_length=255)
    openai_api_key = models.CharField(max_length=255)
    openai_api_base = models.CharField(max_length=255)
    discord_token = models.CharField(max_length=255, blank=True, null=True)
    google_api_key = models.CharField(max_length=255, blank=True, null=True)
    google_cse_id = models.CharField(max_length=255, blank=True, null=True)
    google_maps_api_key = models.CharField(max_length=255, blank=True, null=True)
    home_assistant_token = models.CharField(max_length=255, blank=True, null=True)
    home_assistant_url = models.CharField(max_length=255, blank=True, null=True)