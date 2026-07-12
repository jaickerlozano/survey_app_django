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
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"
# admin.site.register(Choice)
