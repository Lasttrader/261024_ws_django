from .models import Scoring
from django.contrib import admin


class ScoringAdmin(admin.ModelAdmin):

	list_display = ('job_LE', 'marital_LE', 'education_LE', 'default_LE',
                 'housing_LE', 'loan_LE', 'contact_LE', 'month_LE',
                 'poutcome_LE', 'age', 'balance', 'day', 'duration',
                 'campaign', 'pdays', 'previous')
	search_fields = ('feature_1',)
	list_filter = ('feature_2',)


admin.site.register(Scoring)
