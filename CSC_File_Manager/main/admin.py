from django.contrib import admin
from .models import CaseFile
# Register your models here.

#to display the datas from CaseFile in /admin
admin.site.register(CaseFile)