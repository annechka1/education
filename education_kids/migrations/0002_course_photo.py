# Generated by Django 3.2a1 on 2021-02-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education_kids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]