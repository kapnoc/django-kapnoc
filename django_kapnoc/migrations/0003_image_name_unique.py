# Generated by Django 3.1.3 on 2020-11-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_kapnoc', '0002_auto_20201101_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name_unique',
            field=models.CharField(default='', editable=False, max_length=255),
            preserve_default=False,
        ),
    ]
