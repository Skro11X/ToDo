
from django import forms
from decks.models import Task,Deck

class TaskForm(forms.ModelForm):
    deck = forms.ModelChoiceField(queryset=Deck.objects.all(),widget=forms.HiddenInput())
    class Meta:
        model = Task
        fields = '__all__'