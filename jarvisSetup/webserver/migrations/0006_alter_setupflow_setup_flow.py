# Generated by Django 5.0.1 on 2024-01-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webserver', '0005_setupflow_alter_generalcustomization_wake_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setupflow',
            name='setup_flow',
            field=models.CharField(default='home', max_length=100),
        ),
    ]
