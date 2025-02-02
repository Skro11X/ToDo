from django.views.generic import ListView, DetailView, View, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, reverse
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
            "To Do": Task.objects.filter(deck=self.object, status=Task.Status.TO_DO),
            "In Progress": Task.objects.filter(deck=self.object, status=Task.Status.IN_PROGRESS),
            "Done": Task.objects.filter(deck=self.object, status=Task.Status.DONE),
        }
        context['form_class_detail'] = self.form_class(instance=self.object)
        context['form_of_task'] = TaskForm(initial={'deck': self.object.id, 'status': 'TD'})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect('deck-detail', slug=form.instance.slug)


class DeckCreateView(CreateView):
    model = Deck
    form_class = DeckForm


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('deck-detail', kwargs={'slug': self.object.deck.slug})


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('deck-detail', kwargs={'slug': self.object.deck.slug})


class ChangeStatusView(View):
    def post(self, request, *args, **kwargs):
        new_status = request.POST['new_status']
        id_task = request.POST['id_task']
        updated_task = get_object_or_404(Task, pk=id_task)
        updated_task.status = new_status
        updated_task.save()
        return redirect('deck-detail', updated_task.deck.slug)
# Create your views here.
