from dataclasses import fields
from django import forms
from .models import PredResults


class Form(forms.ModelForm):
    class Meta:
        model = PredResults
        fields = ['experience', 'company_size', 'job_title',
                  'remote', 'company_location']
