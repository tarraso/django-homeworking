from django.contrib import admin

from .models import HomeworkSheet, Sentence, Homework, StudentSentence 


class SentenceInline(admin.TabularInline):
    model = Sentence
    extra = 3


class HomeworkSheetAdmin(admin.ModelAdmin):
    inlines = [SentenceInline]
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(HomeworkSheet, HomeworkSheetAdmin);


class StudentSentenceInline(admin.TabularInline):
	model = StudentSentence


class HomeworkAdmin(admin.ModelAdmin):
	inlines = [StudentSentenceInline]

admin.site.register(Homework, HomeworkAdmin)