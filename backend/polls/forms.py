from django.forms import ModelForm
from .models import Question, Choice
import datetime


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]
        help_texts = {
            "question_text": "Texto de la pregunta",
            "pub_date": "Fecha de publicación",
        }