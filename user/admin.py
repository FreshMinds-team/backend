from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Qualification)
admin.site.register(Experience)
admin.site.register(Expertise)
