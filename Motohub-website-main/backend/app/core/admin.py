from django.contrib import admin
from .models import Motorcycle

@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('model', 'type', 'year', 'price')
    search_fields = ('model',)
    list_filter = ('type', 'year')
