from django.contrib import admin
from .models import GenomicProfile


class GroupMemberInline(admin.TabularInline):
    model = GenomicProfile


admin.site.register(GenomicProfile)
