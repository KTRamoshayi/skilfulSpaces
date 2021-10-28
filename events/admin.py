from django.contrib.admin import ModelAdmin, TabularInline, site
from django.db import models
from .models import Event, Registration


class RegistrationInline(TabularInline):
    model = Registration
    extra = 3


class EventAdmin(ModelAdmin):
    list_display = ['title', 'date', 'time', 'departure', 'is_active', 'registrations', 'approved', 'pending']
    list_filter = ['is_active', 'departure']
    inlines = [RegistrationInline]

site.register(Event, EventAdmin)


# class RegistrationAdmin(ModelAdmin):
#     list_display = ['user', 'event', 'approved']
#     list_filter = ['user', 'event', 'approved']

# site.register(Registration, RegistrationAdmin)
