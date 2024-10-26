from django import forms
from .models import Scoring	


class ScoringForm(forms.ModelForm):

    class Meta:
        model = Scoring
        fields = (
            'job_LE', 'marital_LE', 'education_LE', 'default_LE', 'housing_LE',
            'loan_LE', 'contact_LE', 'month_LE', 'poutcome_LE', 'age', 'balance',
            'day', 'duration', 'campaign', 'pdays', 'previous',
        )
