# Generated by Django 3.1.5 on 2022-08-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djaml', '0006_auto_20220825_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='company_size',
            field=models.CharField(choices=[('L', 'L'), ('M', 'M'), ('S', 'S')], default=('L', 'L'), max_length=50),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='job_title',
            field=models.CharField(blank=True, choices=[('Data Scientist', 'Data Scientist'), ('Data Engineer', 'Data Engineer'), ('Machine Learning Engineer', 'Machine Learning Engineer'), ('Research Scientist', 'Research Scientist'), ('Data Science Manager', 'Data Science Manager'), ('Data Architect', 'Data Architect'), ('Big Data Engineer', 'Big Data Engineer'), ('Machine Learning Scientist', 'Machine Learning Scientist')], default=('Data Scientist', 'Data Scientist'), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='remote',
            field=models.CharField(blank=True, choices=[('0', '0'), ('50', '50'), ('100', '100')], default=('0', '0'), max_length=50, null=True),
        ),
    ]
