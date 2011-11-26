from django.contrib import admin
from licensing.models import License


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('license',)

admin.site.register(License, LicenseAdmin)
