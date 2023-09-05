from django.contrib import admin
from .models import Question, Choise, Survey

# Register your models here.

# admin.site.register(Question)
# admin.site.register(Choise)
# admin.site.register(Survey)


class ChoiceInLine(admin.TabularInline):
    model = Choise
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'survey')
    inlines = [ChoiceInLine]


class QuestionInLine(admin.TabularInline):
    model = Question
    estra = 3


@admin.register(Survey)
class SurverAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]
