# Generated by Django 2.2.7 on 2020-01-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200131_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(auto_created=True, blank=True, default=None, max_length=200, null=True),
        ),
    ]
