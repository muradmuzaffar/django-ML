from django.db import models

# Create your models here.


EXPERIENCE_CHOICES = [
    ("EN", ("EN")),
    ("EX", ("EX")),
    ("MI", ("MI")),
    ("SE", ("SE")),

]

SIZE_CHOICES = [
    ("L", ("L")),
    ("M", ("M")),
    ("S", ("S")),

]

JOB_CHOICES = [
    ("Data Scientist", ("Data Scientist")),
    ("Data Engineer", ("Data Engineer")),
    ("Machine Learning Engineer", ("Machine Learning Engineer")),
    ("Research Scientist", ("Research Scientist")),
    ("Data Science Manager", ("Data Science Manager")),
    ("Data Architect", ("Data Architect")),
    ("Big Data Engineer", ("Big Data Engineer")),
    ("Machine Learning Scientist", ("Machine Learning Scientist")),

]


REMOTE_CHOICES = [
    ("0", ("In office")),
    ("50", ("Hybrid")),
    ("100", ("Full Remote")),

]

LOCATION_CHOICES = [
    ("US", ("USA")),
    ("GB", ("Great Britain")),
    ("CA", ("Canada")),
    ("IN", ("India")),
    ("FR", ("France")),
    ("DE", ("Deutchland")),
    ("ES", ("Spain")),
    ("GR", ("Greece")),
    ("AT", ("Austria")),

]


class PredResults(models.Model):
    experience = models.CharField(
        max_length=50, choices=EXPERIENCE_CHOICES, default=REMOTE_CHOICES[0])

    company_size = models.CharField(
        max_length=50, choices=SIZE_CHOICES, default=SIZE_CHOICES[0])

    job_title = models.CharField(
        max_length=50, choices=JOB_CHOICES, blank=True, null=True, default=JOB_CHOICES[0])

    remote = models.CharField(
        max_length=50, choices=REMOTE_CHOICES, blank=True, null=True, default=REMOTE_CHOICES[0])

    company_location = models.CharField(
        max_length=50, choices=LOCATION_CHOICES, blank=True, null=True, default=LOCATION_CHOICES[0])

    salary = models.IntegerField(blank=True, null=True)
