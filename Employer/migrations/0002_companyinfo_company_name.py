# Generated by Django 3.0.4 on 2020-05-29 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='company_name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]