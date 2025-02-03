from django import forms
from decks.models import Deck


class DeckForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Deck
        fields = ['name',]
        labels = {
            'name': 'Название доски',
        }
