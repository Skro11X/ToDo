from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import redirect
from decks.forms import DeckForm, TaskForm
from decks.models import Deck, Task


class DeckListView(ListView):
    model = Deck
    queryset = Deck.objects.all()
    template_name = 'decks/deck_list.html'
    form_class = DeckForm
    context_object_name = "decks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


class DeckDetailView(DetailView):
    model = Deck
    queryset = Deck.objects.all()
    template_name = 'decks/deck_detail.html'
    form_class = DeckForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks_groups'] = {
            ("To Do", "TD"): Task.objects.filter(deck=self.object, status=Task.Status.TO_DO),
            ("In Progress", "IP"): Task.objects.filter(deck=self.object, status=Task.Status.IN_PROGRESS),
            ("Done", "DN"): Task.objects.filter(deck=self.object, status=Task.Status.DONE),
        }
        context['form_class_detail'] = self.form_class(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect('deck-detail', slug=form.instance.slug)


class DeckCreateView(CreateView):
    model = Deck
    form_class = DeckForm
    template_name = "decks/deck_create.html"


class DeckDeleteView(DeleteView):
    model = Deck
    template_name = "decks/delete.html"
    success_url = reverse_lazy("deck-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lust_page'] = self.request.META.get('HTTP_REFERER', '/')
        return context
