# Generated by Django 3.1.5 on 2022-08-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djaml', '0003_auto_20220825_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='experience',
            field=models.CharField(choices=[('EN', 'EN'), ('EX', 'EX'), ('MI', 'MI'), ('SE', 'SE')], default='EN', max_length=50),
        ),
    ]