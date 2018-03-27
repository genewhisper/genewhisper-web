from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

FILE_TYPE_CHOICES = (
    ('FASTQ', 'FASTQ file format'),
    ('VCF', 'VCF file format'),
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - Still Researching'),
)

ALLOW_SALE = (
    ('YES', 'Allow Sale'),
    ('NO', 'Don Allow To Sale'),
)

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


class GenomicProfile(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    middle_init = models.CharField(max_length=100, blank=True)
    physical_address = models.CharField(max_length=200, blank=False)
    apt_number = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    zip = models.IntegerField(blank=False)
    phone = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    alternate_contact_name_and_number = models.TextField()
    relationship = models.CharField(max_length=30, blank=True, null=True)
    mailing_address = models.TextField(blank=True, null=True)

    height_ft = models.PositiveIntegerField(blank=False)
    height_inch = models.PositiveIntegerField(blank=False)
    weight = models.PositiveIntegerField(blank=False)
    dob = models.DateField(blank=False)
    age = models.PositiveIntegerField(blank=False)
    race = models.CharField(max_length=56, choices=RACE_CHOICES, blank=False)
    gender = models.CharField(max_length=56, choices=GENDER_CHOICES, blank=False)

    referral_name = models.CharField(max_length=100, blank=True, null=True)
    referral_contact = models.TextField(blank=True, null=True)

    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    job_file = models.FileField(upload_to='uploads/', blank=True)
    file_format = models.CharField(max_length=56, choices=FILE_TYPE_CHOICES, blank=False)
    submitted_date = models.DateField(auto_now_add=True)
    allow_sale = models.CharField(max_length=56, choices=ALLOW_SALE, blank=False)

    def get_absolute_url(self):
        return reverse("profiles:genomic_profile_details", kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id)
