# Generated by Django 3.1.5 on 2022-08-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djaml', '0004_auto_20220825_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='experience',
            field=models.CharField(choices=[('EN', 'EN'), ('EX', 'EX'), ('MI', 'MI'), ('SE', 'SE')], max_length=50),
        ),
    ]
