from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'last_name', 'first_name', 'email', 'phone_number')
    list_filter = ('gender', 'created_at')
    search_fields = ('registration_number', 'last_name', 'first_name', 'email')
    ordering = ('last_name', 'first_name')
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender')
        }),
        ('Coordonnées', {
            'fields': ('email', 'phone_number', 'address')
        }),
        ('Informations académiques', {
            'fields': ('registration_number',)
        }),
    )
