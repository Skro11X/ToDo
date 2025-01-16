from django.db import models
from django.urls import reverse
from mptt.models import TreeForeignKey, MPTTModel


class TasksDeck(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(max_length=100, verbose_name="Slug")

    def get_absolute_url(self):
        return reverse("deck-detail", kwargs={"slug": self.slug})


class Task(MPTTModel):
    _status_choices = [
        ("TD", "to do"),
        ("IP", "in progress"),
        ("DN", "done"),
    ]

    status = models.CharField(default=False, choices=_status_choices, max_length=20, verbose_name="Status")
    label = models.CharField(max_length=100 , verbose_name="Label")
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField(max_length=100, verbose_name="Slug")
    deck = models.ForeignKey(TasksDeck, on_delete=models.CASCADE, verbose_name="Deck")
    parent = TreeForeignKey("self", on_delete=models.CASCADE, verbose_name="Parent", null=True, blank=True)




