from django.db import models
from django.urls import reverse


class Deck(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(max_length=100, verbose_name="Slug")

    def get_absolute_url(self):
        return reverse("deck-detail", kwargs={"slug": self.slug})


class Task(models.Model):
    _status_choices = [
        ("TD", "to do"),
        ("IP", "in progress"),
        ("DN", "done"),
    ]


    status = models.CharField(default=False, choices=_status_choices, max_length=20, verbose_name="Status")
    label = models.CharField(max_length=100, verbose_name="Label")
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField(max_length=100, verbose_name="Slug")
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, verbose_name="Deck")

    def get_available_statuses(self):
        all_statuses = [status[0] for status in self._status_choices]
        my_status = all_statuses.index(self.status)
        return [all_statuses[i] for i in range(len(all_statuses)) if my_status == i + 1 or my_status == i - 1]
