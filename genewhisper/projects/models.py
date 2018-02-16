from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICES = (
    ('NEW', 'New Project'),
    ('EX', 'Existing Project'),
)

FILE_TYPE_CHOICES = (
    ('FASTQ', 'FASTQ file format'),
    ('VCF', 'VCF file format'),
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - Still Researching'),
)


class Project(models.Model):
    name = models.CharField(max_length=100 )
    position = models.CharField(max_length=60, blank=True)
    company = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    description = models.TextField()
    project_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    job_file = models.FileField(upload_to='uploads/', blank=True)
    file_format = models.CharField(max_length=56, choices=FILE_TYPE_CHOICES, blank=False)
    submitted = models.DateField(auto_now_add=True)
    project_date = models.DateField(blank=True, null=True)
    project_price = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("projects:project_details", kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id)
