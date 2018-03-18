from django.db import models
from django.urls import reverse
from accounts.models import CompanyRegistration
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

RACE_CHOICES = (
    ('C', 'Caucasian'),
    ('AA', 'African American '),
    ('H', 'Hispanic'),
    ('AP', 'Asian/Pacific'),
    ('NA', 'Native American'),
    ('O', 'Other')
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

CLINICAL_TRIAL_TYPE_CHOICES = (
    ('C', 'Cardiology'),
    ('CAN', 'Cancer'),
    ('N', 'Neurology'),
    ('O', 'Oncology'),
    ('M', 'Metabolism'),
    ('P', 'Pediatrics'),

)


# Create your models here.
class ClinicalTrial(models.Model):
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.ForeignKey(User, null=True, blank=True, related_name='company', on_delete=models.CASCADE)
    identifier = models.CharField(max_length=24, blank=False)
    official_title = models.TextField(blank=True)
    variants = models.CharField(blank=True, null=False, max_length=24)
    genes = models.CharField(blank=True, null=False, max_length=24)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    number_of_participants = models.PositiveIntegerField(blank=False)
    offer_price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    max_age = models.PositiveIntegerField(blank=False)
    race = models.CharField(max_length=56, choices=RACE_CHOICES, blank=False)
    gender = models.CharField(max_length=56, choices=GENDER_CHOICES, blank=False)
    clinical_trial_type = models.CharField(max_length=56, choices=CLINICAL_TRIAL_TYPE_CHOICES, blank=False)
    min_age = models.PositiveIntegerField(blank=False)

    submitted_date = models.DateField(auto_now_add=True)

    brief_summary = models.TextField(blank=True)
    detailed_description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("marketplace:clinical_trial_details", kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id)

    def clean(self):
        if self.variants == '' and self.genes == '':
            raise ValidationError('Genes or Variants should be submitted')
