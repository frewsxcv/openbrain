from django.contrib import admin
from core.models import Category
from core.models import Topic
from core.models import Video
from core.models import License


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('topic', 'source_url', 'license')


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('license',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(License, LicenseAdmin)
