from django import template
from decks.models import Deck

register = template.Library()


@register.inclusion_tag('decks/show_all_decks.html')
def show_all_decks():
    decks = Deck.objects.all()
    return {'decks': decks}
