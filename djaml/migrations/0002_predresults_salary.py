# Generated by Django 3.1.5 on 2022-08-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djaml', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predresults',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]