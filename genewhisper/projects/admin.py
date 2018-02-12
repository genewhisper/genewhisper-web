from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'submitted', 'project_date', 'project_price')
    list_filter = ('submitted', 'project_date')
    readonly_fields = ('submitted',)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'description')
        }),
        ('Contact Information', {
            'classes': ('collapse',),
            'fields': ('position', 'company', 'address', 'phone', 'web')
        }),
        ('Job Information', {
            'classes': ('collapse',),
            'fields': ('project_status', 'priority', 'job_file', 'submitted')
        }),
        ('Quote Admin', {
            'classes': ('collapse',),
            'fields': ('project_date', 'project_price', 'username')
        }),
    )


admin.site.register(Project, ProjectAdmin)
