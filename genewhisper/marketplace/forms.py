from django import forms
from django.forms import ModelForm
from django.forms.widgets import Select
from marketplace.models import ClinicalTrial


class ClinicalTrialForm(ModelForm):
    class Meta:
        model = ClinicalTrial

        fields = [

            'identifier', 'official_title', 'variants', 'genes',
            'start_date', 'end_date', 'number_of_participants',
            'offer_price', 'max_age', 'race', 'gender', 'clinical_trial_type',
            'min_age', 'brief_summary', 'detailed_description'
        ]
