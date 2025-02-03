from decks.views.decks_views import DeckListView, DeckCreateView, DeckDetailView, DeckDeleteView
from decks.views.tasks_views import TaskUpdateView, TaskCreateView, ChangeStatusView, TaskDeleteView

__all__ = ['DeckListView', 'DeckCreateView', 'DeckDetailView', "DeckDeleteView",
           "TaskUpdateView", "TaskCreateView", "ChangeStatusView", "TaskDeleteView"]