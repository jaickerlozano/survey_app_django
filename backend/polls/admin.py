from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoicesInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information (Esto es editable y es el título del conjunto de campos)", 
            {  
             "fields": ["pub_date"],
             "classes": ["collapse"],
            }
         ),
    ]
    inlines = [ChoicesInline]


admin.site.register(Question, QuestionAdmin)
