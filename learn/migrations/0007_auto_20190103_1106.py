# Generated by Django 2.0.2 on 2019-01-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]
