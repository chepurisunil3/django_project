# Generated by Django 3.1.1 on 2020-09-15 16:41

from django.db import migrations, models
import myFirstApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0002_firstapp_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstapp',
            name='isAvailable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='firstapp',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=myFirstApp.models.upload_image_path),
        ),
    ]