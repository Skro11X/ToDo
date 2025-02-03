from django.db import models
from django.urls import reverse


class Deck(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(max_length=100, verbose_name="Slug", unique=True)

    def get_absolute_url(self):
        return reverse("deck-detail", kwargs={"slug": self.slug})


class Task(models.Model):
    class Status(models.TextChoices):
        TO_DO = "TD", "To Do"
        IN_PROGRESS = "IP", "In Progress"
        DONE = "DN", "Done"

    status = models.CharField(default=False, choices=Status.choices, max_length=20, verbose_name="Status")
    label = models.CharField(max_length=100, verbose_name="Label")
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField(max_length=100, verbose_name="Slug", unique=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, verbose_name="Deck")

    def get_available_statuses(self):
        my_choice = self.status
        available_statuses = dict(self.Status.choices)
        available_statuses.pop(my_choice)
        return available_statuses



    def __str__(self):
        return self.slug
