from django.contrib import admin
from .models import Question,Choice

admin.site.site_header="Gaming admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question']}),
                ('Date Information',{'fields':['pub_date'],'classes':
                ['collapse']}),] 
    inlines = [ChoiceInline]    

admin.site.register(Question,QuestionAdmin)               

# admin.site.register(Question)
# admin.site.register(Choice)
