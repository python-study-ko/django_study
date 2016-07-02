from django.contrib import admin

# Register your models here.
from polls.models import Question,Choice

# 다중 테이블을 보기 위한 choice classes
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('질문 날짜',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 레코드 리스트 항목 지정
    list_display = ('question_text','pub_date')
    # 필터 추가
    list_filter = ['pub_date']
    # 검색박스 추가
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)