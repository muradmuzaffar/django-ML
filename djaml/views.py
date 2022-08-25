from django.shortcuts import render
import pandas as pd
import numpy as np
from .forms import Form
from .models import PredResults

# Create your views here.


def index(request):
    form = Form(request.POST or None)
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            ex_level = form.cleaned_data['experience']
            comp_size = form.cleaned_data['company_size']
            remote = form.cleaned_data['remote']
            job_title = form.cleaned_data['job_title']
            company_location = form.cleaned_data['company_location']

            inputs = pd.DataFrame({'experience_level': ex_level,
                                   'company_size': comp_size,
                                   'remote_ratio': remote,
                                   'job_title': job_title,
                                   'company_location': company_location},  index=[0])

            model = pd.read_pickle('./ml/model.pkl')

            data = pd.read_csv('./ml/ds_salaries_new.csv',
                               index_col=0).drop(columns=['salary_in_usd'])
            df = pd.concat([inputs, data], axis=0)

            encode = ['experience_level', 'company_size',
                      'remote_ratio', 'job_title', 'company_location']
            for col in encode:
                dummy = pd.get_dummies(df[col], prefix=col)
                df = pd.concat([df, dummy], axis=1)
                del df[col]
            df = df[:1]
            # df['salary_in_usd'] = df['salary_in_usd'].apply(
            #     pd.to_numeric).astype('Int64')
            df = df.loc[:, ~df.columns.duplicated()].copy()

            # global pred
            pred = model.predict(df)
            # PredResults.objects.create(
            #     experience=inputs['experience_level'], company_size=inputs['company_size'],
            #     remote=inputs['remote_ratio'], job_title=inputs['job_title'])

        return render(request, 'index.html', {"pred": pred})
    else:
        return render(request, 'index.html', {'form': form})
