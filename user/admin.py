from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *

class CustomDoctorAdmin(UserAdmin):
    add_form = CustomDoctorCreationForm
    form = CustomDoctorChangeForm
    model = Doctor
    list_display = ('email', 'username','is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','dob','type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'first_name','last_name','is_staff', 'is_active','dob','type','gender')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
class CustomPatientAdmin(UserAdmin):
    add_form = CustomPatientCreationForm
    form = CustomPatientChangeForm
    model = Patient
    list_display = ('email', 'username','is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','dob','type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'first_name','last_name','is_staff', 'is_active','dob','type')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Patient,CustomPatientAdmin)
admin.site.register(Doctor,CustomDoctorAdmin)
admin.site.register(Qualification)
admin.site.register(Experience)
admin.site.register(Expertise)
admin.site.register(User)
