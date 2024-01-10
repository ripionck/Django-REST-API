from django.contrib import admin
from . import models

# Register your models here.


class Specialization(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class Designation(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(models.AvailableTime)
admin.site.register(models.Specialization, Specialization)
admin.site.register(models.Designation, Designation)
admin.site.register(models.Doctor)
admin.site.register(models.Review)
