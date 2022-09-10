from django.contrib import admin
from .models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['symbol']
    
admin.site.register(Company , CompanyAdmin)
