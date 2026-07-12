from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone
from .forms import QuestionForm

# Create your views here.
class QuestionCreateView(generic.CreateView):
    form_class = QuestionForm
    template_name = "polls/question_create.html"
    success_url = "/polls"


class QuestionUpdateView(generic.UpdateView):
    model = Question
    fields = ["question_text", "pub_date"]
    template_name = "polls/question_update.html"
    success_url = "/polls"


class QuestionDeleteView(generic.DeleteView):
    model = Question
    template_name = "polls/question_delete.html"
    success_url = "/polls"


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected__choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, 
            "polls/detail.html",
            {
                "question": question,
                "error_message": "No elegiste una respuesta",
            }
        )
    else:
        selected__choice.votes = F("votes") + 1
        selected__choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

    return HttpResponse("You're voting on question %s" % question_id)


