from django.forms import ModelForm
from decks.models import TasksDeck

class DeckForm(ModelForm):

    class Meta:
        model = TasksDeck
        fields = '__all__'