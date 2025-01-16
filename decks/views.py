from django.shortcuts import render
from django.views.generic import ListView, DetailView

from decks.forms.deck_form import DeckForm
from decks.models import TasksDeck, Task

class DeckListView(ListView):
    model = TasksDeck
    queryset = TasksDeck.objects.all()
    template_name = 'decks/deck_list.html'


class DeckDetailView(DetailView):
    model = TasksDeck
    queryset = TasksDeck.objects.all()
    template_name = 'decks/deck_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(deck=self.object)
        context['form_class'] = DeckForm(instance=self.object)
        return context




# Create your views here.
