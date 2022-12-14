# Generated by Django 3.1.5 on 2022-08-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djaml', '0009_auto_20220825_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='predresults',
            name='company_location',
            field=models.CharField(blank=True, choices=[('US', 'USA'), ('GB', 'Great Britain'), ('CA', 'Canada'), ('IN', 'India'), ('FR', 'France'), ('DE', 'Deutchland'), ('ES', 'Spain'), ('GR', 'Greece'), ('AT', 'Austria')], default=('US', 'USA'), max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='predresults',
            name='employee_residence',
            field=models.CharField(blank=True, choices=[('US', 'USA'), ('GB', 'Great Britain'), ('CA', 'Canada'), ('IN', 'India'), ('FR', 'France'), ('DE', 'Deutchland'), ('ES', 'Spain'), ('GR', 'Greece')], default=('US', 'USA'), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='experience',
            field=models.CharField(choices=[('EN', 'EN'), ('EX', 'EX'), ('MI', 'MI'), ('SE', 'SE')], default=('0', 'Offline'), max_length=50),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='remote',
            field=models.CharField(blank=True, choices=[('0', 'Offline'), ('50', 'Hybrid'), ('100', 'Full Remote')], default=('0', 'Offline'), max_length=50, null=True),
        ),
    ]
