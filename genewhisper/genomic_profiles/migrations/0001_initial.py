# Generated by Django 2.0.1 on 2018-03-28 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenomicProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_init', models.CharField(blank=True, max_length=100)),
                ('physical_address', models.CharField(max_length=200)),
                ('apt_number', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip', models.IntegerField()),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('alternate_contact_name_and_number', models.TextField()),
                ('relationship', models.CharField(blank=True, max_length=30, null=True)),
                ('mailing_address', models.TextField(blank=True, null=True)),
                ('height_ft', models.PositiveIntegerField()),
                ('height_inch', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('race', models.CharField(choices=[('C', 'Caucasian'), ('AA', 'African American '), ('H', 'Hispanic'), ('AP', 'Asian/Pacific'), ('NA', 'Native American'), ('O', 'Other')], max_length=56)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=56)),
                ('referral_name', models.CharField(blank=True, max_length=100, null=True)),
                ('referral_contact', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('U', 'Urgent - 1 week or less'), ('N', 'Normal - 2 to 4 weeks'), ('L', 'Low - Still Researching')], max_length=40)),
                ('job_file', models.FileField(blank=True, upload_to='uploads/')),
                ('file_format', models.CharField(choices=[('FASTQ', 'FASTQ file format'), ('VCF', 'VCF file format')], max_length=56)),
                ('submitted_date', models.DateField(auto_now_add=True)),
                ('allow_sale', models.CharField(choices=[('YES', 'Allow Sale'), ('NO', 'Don Allow To Sale')], max_length=56)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
