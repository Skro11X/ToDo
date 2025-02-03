from django.urls import path
from decks.views import DeckListView, DeckDetailView, DeckCreateView, DeckDeleteView ,ChangeStatusView, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', DeckListView.as_view(), name='deck-list'),
    path('create/', DeckCreateView.as_view(), name='deck-create'),
    path('<slug:slug>/', DeckDetailView.as_view(), name='deck-detail'),
    path('delete/<int:pk>/', DeckDeleteView.as_view(), name='deck-delete'),
    path('task/change_status_task/', ChangeStatusView.as_view(), name='change-status-task'),
    path('task/create_task/<int:id>/', TaskCreateView.as_view(), name='task-create'),
    path('task/<slug:slug>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]