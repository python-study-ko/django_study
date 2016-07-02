from django.contrib import admin

# Register your models here.
from polls.models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 내용',{'fields':['question_text']}),
        ('질문 날짜',{'fields':['pub_date'],'classes':['collapse']}),
    ]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)