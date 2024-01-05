# Generated by Django 5.0.1 on 2024-01-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralCustomization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistant_name', models.CharField(max_length=100)),
                ('wake_word', models.CharField(max_length=50)),
                ('system_prompt', models.CharField(max_length=100)),
                ('llm_model', models.CharField(max_length=50)),
                ('voice_diarization', models.CharField(max_length=50)),
            ],
        ),
    ]
