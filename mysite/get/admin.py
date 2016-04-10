from django.contrib import admin

# Register your models here.

from .models import NewsEvents,Exercise

class NewsEventsAdmin(admin.ModelAdmin):
    fields = ['date', 'title_en', 'title_ne', 'content_en', 'content_ne']
    list_display = ('date', 'title_en')

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'questions')

admin.site.register(NewsEvents, NewsEventsAdmin)

admin.site.register(Exercise, ExerciseAdmin)


