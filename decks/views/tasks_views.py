from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, reverse
from decks.forms import TaskForm
from decks.models import Task
from decks.models import Deck


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create_task.html"

    def get_initial(self):
        initial = super().get_initial()
        data_for_form = dict()
        deck_id = self.kwargs.get('id', 0)
        data_for_form["status"] = self.request.GET.get('status')
        data_for_form['deck_id'] = get_object_or_404(Deck, id=deck_id)
        initial["deck"] = data_for_form["deck_id"]
        initial["status"] = data_for_form["status"]
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        deck_id = self.kwargs.get('id', 0)
        # print(data_for_form['deck_id'], status)
        # context['form'].fields['deck'] = data_for_form['deck_id']
        # context['form'].fields['status'] = status
        context['deck'] = deck_id
        return context

    def get_success_url(self):
        return reverse('deck-detail', kwargs={'slug': self.object.deck.slug})


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('deck-detail', kwargs={'slug': self.object.deck.slug})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/delete.html"

    def get_success_url(self):
        return reverse('deck-detail', kwargs={'slug': self.object.deck.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lust_page'] = self.request.META.get('HTTP_REFERER', '/')
        return context


class ChangeStatusView(View):
    def post(self, request, *args, **kwargs):
        new_status = request.POST['new_status']
        id_task = request.POST['id_task']
        updated_task = get_object_or_404(Task, pk=id_task)
        updated_task.status = new_status
        updated_task.save()
        return redirect('deck-detail', updated_task.deck.slug)
