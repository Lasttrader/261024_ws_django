from django.db import models


class Scoring(models.Model):

    job_LE = models.CharField(max_length=200)
    marital_LE = models.CharField(max_length=200)
    education_LE = models.CharField(max_length=200)
    default_LE = models.CharField(max_length=200)
    housing_LE = models.CharField(max_length=200)
    loan_LE = models.CharField(max_length=200)
    contact_LE = models.CharField(max_length=200)
    month_LE = models.CharField(max_length=200)
    poutcome_LE = models.CharField(max_length=200)
    age = models.IntegerField()
    balance = models.IntegerField()
    day = models.IntegerField()
    duration = models.IntegerField()
    campaign = models.IntegerField()
    pdays = models.IntegerField()
    previous = models.IntegerField()
