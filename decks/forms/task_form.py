
from django import forms
from decks.models import Task,  Deck

class TaskForm(forms.ModelForm):
    deck = forms.ModelChoiceField(queryset=Deck.objects.all(), widget=forms.HiddenInput())
    status = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Task
        exclude = ['slug']
