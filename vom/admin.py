from django.contrib import admin
from vom.models import *
from django.contrib.auth import get_user_model

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'birthday')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk' ,'category', '__unicode__', 'date')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk' , '__unicode__', 'date')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk' , 'writer', '__unicode__', 'date')

admin.site.register(get_user_model(), MyUserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(CategoryOfQuestion, CategoryAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Constellation)
admin.site.register(Item)
admin.site.register(Status, StatusAdmin)