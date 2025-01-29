from django.forms import ModelForm
from decks.models import Deck


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = '__all__'
