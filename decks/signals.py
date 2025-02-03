from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from unidecode import unidecode
import uuid
from decks.models import Deck
from decks.models import Task


@receiver(pre_save, sender=Task)
def get_random_slag_task(sender, instance, **kwargs):

    instance.slug = slugify(unidecode(instance.label), allow_unicode=True)
    while sender.objects.filter(slug=instance.slug).exists():
        instance.slug = instance.slug + uuid.uuid4().hex[:8]


@receiver(pre_save, sender=Deck)
def get_random_slag_deck(sender, instance, **kwargs):
    instance.slug = slugify(unidecode(instance.name), allow_unicode=True)
    while sender.objects.filter(slug=instance.slug).exists():
        instance.slug = instance.slug + uuid.uuid4().hex[:8]


