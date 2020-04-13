from django.contrib import admin
from .models import *

@admin.register(File)

class ApiAdmin(admin.ModelAdmin):
    pass
