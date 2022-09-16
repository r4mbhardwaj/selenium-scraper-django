from django.contrib import admin
from .models import *


class PlanAdmin(admin.ModelAdmin):
    list_display = ('price', 'extra_data', 'benifits')


admin.site.register(Plan, PlanAdmin)
