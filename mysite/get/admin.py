from django.contrib import admin

# Register your models here.

from .models import NewsEvents,ExerciseQuestion,ExerciseChoice

class NewsEventsAdmin(admin.ModelAdmin):
    fields = ['date', 'title', 'content']
    list_display = ('date', 'title')

class ExerciseQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'my_answers')

admin.site.register(NewsEvents, NewsEventsAdmin)

admin.site.register(ExerciseQuestion, ExerciseQuestionAdmin)

admin.site.register(ExerciseChoice)

